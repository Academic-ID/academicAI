import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from client import client, parse_JSON, default_model, vision_model
import pandas as pd
import shutil
from tqdm.notebook import tqdm
from PyPDF2 import PdfReader
from docx import Document
import concurrent.futures
import tiktoken
from functools import wraps
import time

def retry(max_retries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries < max_retries:
                        print(f"Retry {retries}/{max_retries} for {func.__name__} due to: {str(e)}")
                        time.sleep(delay * retries)
                    else:
                        raise e
        return wrapper
    return decorator

@retry()
def get_summary(doc_text, user_instruction):
    """Returns a json object with is_text_present and summary keys. is_text_present is a boolean value indicating whether the text is present and readable. summary is the summary of the document."""
    system_prompt=f"{user_instruction}\n\n{doc_text}"
    sum_fn = [
    {
      'type': 'function',
      'function': {
        'name': 'collect_summary',
        'description': "This function requires the assistant to provide two parameters. First, the assistant must determine if the provided text is not empty and is legible enough to provide a summary. If it is, the second parameter should include that summary. If the text is not present or not legible, the summary parameter should be returned as 'N/A'",
        'parameters': {
          'type': 'object',
          'properties': {
            'is_text_present': {
              'type': 'boolean',
              'description':
                'The text is being extracted from documents include PDF files. There are occasions where the text extraction fails and no content is returned or the content is nonsensical. If the content is present, return True, if not present (or text is not capable of being summarised), return False.',
            },
            'summary': {
              'type': 'string',
              'description':
                'The summary of the document as per the instructions set out in the system message. If the text is not present or not legible, return "N/A".',
            },
          },
          'required': ['is_text_present', 'summary'],
        },
      },
    }]
    response = client.chat.completions.create(
                    model=default_model,
                    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": f'{user_instruction}\n\nTEXT:\n\n{doc_text}'}],
                    max_tokens=750,
                    temperature=0.1,
                    tools=sum_fn,
                    tool_choice={ 'type': 'function', 'function': { 'name': 'collect_summary' } },        
                )
    response_message = response.choices[0].message
    tool_call_args = response_message.tool_calls[0].function.arguments
    return parse_JSON(tool_call_args)

def search_and_extract_text(source_folder, destination_folder, keywords):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    results = []
    count = 0
    for filename in os.listdir(source_folder):        
        file_path = os.path.join(source_folder, filename)
        matched_pages_text = []
        if file_path.endswith('.pdf'):
            reader = PdfReader(file_path)
            new_filename = filename
            for i, page in enumerate(reader.pages):
                text_content = page.extract_text() or ''
                if any(keyword.lower() in text_content.lower() for keyword in keywords):
                    count += 1
                    matched_pages_text.append(
                        {'page_number': i+1, 'text_content': text_content})
            if matched_pages_text:
                results.append({'filename': new_filename,
                               'matches': matched_pages_text})
            shutil.move(file_path, os.path.join(
                    destination_folder, new_filename))
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            text_content = ' '.join(para.text for para in doc.paragraphs)
            if any(keyword.lower() in text_content.lower() for keyword in keywords):
                count += 1
                results.append(
                    {'filename': filename, 'text_content': text_content})
            shutil.move(file_path, destination_folder)
        else:
            print(f'Unsupported file format: {filename}')
    
    return results, count

def process_page(task, result, pbar):
    filename = result['filename']
    pages_data = []
    encoding = tiktoken.get_encoding("cl100k_base")
    if 'matches' in result:
        for match in result['matches']:
            page_number = match['page_number']
            text_content = match['text_content']
            encoded_text = encoding.encode(text_content)
            num_tokens = len(encoded_text)
            if num_tokens > 100000:                
                text_content = encoding.decode(encoded_text[:100000])
            ai_res = get_summary(text_content, task)
            if ai_res["is_text_present"] and len(ai_res["summary"]) > 10:
                pages_data.append({
                    'Filename': filename,
                    'Page Number (of file)': page_number,
                    'Text Content': text_content,
                    'AI Summary': ai_res["summary"],
                })
            pbar.update(1)
    elif 'text_content' in result:
        text_content = result['text_content']
        encoded_text = encoding.encode(text_content)
        num_tokens = len(encoded_text)
        if num_tokens > 100000:                
            text_content = encoding.decode(encoded_text[:100000])
        ai_res = get_summary(text_content, task)
        if ai_res["is_text_present"] and len(ai_res["summary"]) > 10:
            pages_data.append({
                'Filename': filename,
                'Text Content': text_content,
                'AI Summary': ai_res["summary"]
            })
        pbar.update(1)
    return pages_data

def process_pages_parallel(task, results, pbar, max_workers):
    data_for_excel = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(
            process_page, task, result, pbar): index for index, result in enumerate(results, start=1)}
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            data_for_excel.extend(future.result())            

    return data_for_excel

def write_to_excel(data, filepath):
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)    

    # Check if the file exists
    if os.path.isfile(filepath):
        os.remove(filepath)

    writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Get workbook and worksheet for formatting
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Set column width to autofit and add word wrap
    format = workbook.add_format({'text_wrap': True, 'valign': 'vcenter', 'font_name': 'Arial'})
    worksheet.set_column('A:A', 20, format)
    worksheet.set_column('B:B', 10, format)
    worksheet.set_column('C:C', 60, format)
    worksheet.set_column('D:D', 60, format)

    # Save the result
    writer.close()

def process(keywords, task, source_folder_path, destination_folder_path, max_workers=5):
    excel_file_path = f'{destination_folder_path}/00. Summaries.xlsx'
    results, count = search_and_extract_text(source_folder_path, destination_folder_path, keywords)
    pbar = tqdm(total=count)
    data_for_excel = process_pages_parallel(task, results, pbar, max_workers )
    write_to_excel(data_for_excel, excel_file_path)
    return f'Overivew saved at: {excel_file_path}'