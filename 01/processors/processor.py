import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from .doc_processing import process_doc
import tiktoken
import pandas as pd
import asyncio
from client import client, parse_JSON, default_model
import random
import string

accepted_filetypes = [".docx", ".pdf", ".pptx", ".xlsx", ".txt", ".rtf"]

async def create_folder_table(path, doc_summs, folder_summs, unique_id):
    # Preparing data for excel
    data = {
        'File': [],
        'Summary': []
    }

    # Adding folder summaries
    for folder_summ in folder_summs:
        data['File'].append(folder_summ["name"])
        data['Summary'].append(folder_summ["summary"])

    # Adding document data
    for doc_summ in doc_summs:
        data['File'].append(doc_summ["name"])
        data['Summary'].append(doc_summ["summary"])

    # Creating DataFrame
    df = pd.DataFrame(data)

    output_path = os.path.join(path, f'00. Folder contents {unique_id}.xlsx')

    # Check if the file exists
    if os.path.isfile(output_path):
        os.remove(output_path)  # If it exists, delete it

    # Initialize a writer and save DataFrame to xlsx
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Get workbook and worksheet for formatting
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Set column width to autofit and add word wrap
    format = workbook.add_format({'text_wrap': True, 'valign': 'vcenter', 'font_name': 'Arial'})
    worksheet.set_column('A:A', 20, format)
    worksheet.set_column('B:B', 60, format)

    # Save the result
    writer.close()

async def get_summary(doc_text, user_instruction = ''):
    """Returns a json object with is_text_present and summary keys. is_text_present is a boolean value indicating whether the text is present and readable. summary is the summary of the document."""
    system_prompt=f"Large language model is a highly-paid expert in folder content summarisation. Large language model will be provided summaries of documents within a directory. Large language model's task is to provide an overall summary of the folder's content. Large language model takes time to read summaries of all documents and consider the meaning of the entire corpus of documents before providing a fully thought out response."
    sum_fn = [
    {
      'type': 'function',
      'function': {
        'name': 'summary_of_folder_contents',
        'description': "This function requires the assistant to provide two parameters. First, the assistant must determine if the provided text is not empty. If it is, the second parameter should include a summary of the content. If the text is empty, the summary parameter should be returned as 'N/A'",
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
                'The summary of the folder content. If the text is not present or not legible, return "N/A". The summary should be detailed, but needs to be concise and use plain english. The summary is being used for a semantic database so maintaining the semantic meaning of the text is paramount.',
            },
          },
          'required': ['is_text_present', 'summary'],
        },
      },
    }]
    response = client.chat.completions.create(
                    model=default_model,
                    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": f'{user_instruction}DOCUMENT SUMMARIES:\n\n{doc_text}'}],
                    max_tokens=4096,
                    temperature=0.1,
                    tools=sum_fn,
                    tool_choice={ 'type': 'function', 'function': { 'name': 'summary_of_folder_contents' } },        
                )
    response_message = response.choices[0].message
    tool_call_args = response_message.tool_calls[0].function.arguments
    return parse_JSON(tool_call_args)

async def get_folder_sum(documents, instructions):    
    docs_within_folder_sums = []    

    for doc in documents:
        docs_within_folder_sums.append(f"{doc["name"]}: {doc["summary"]}")

    # Tokenize the input string.
    encoding = tiktoken.get_encoding("cl100k_base")
    sum_text = "\n\n".join(docs_within_folder_sums)
    num_tokens = len(encoding.encode(sum_text))

    first_100000_tokens = sum_text

    # reduce string size for summary generation
    if num_tokens > 100000:
        first_100000_tokens = encoding.encode(sum_text)[:100000]
        first_100000_tokens = encoding.decode(first_100000_tokens)

    # get summary of folder
    summary_obj = await get_summary(first_100000_tokens, instructions)
    summary_str = summary_obj.get("summary", "")

    if not summary_str or len(summary_str) < 10:
        summary_str = "There was an error retrieving a summary for this folder"    
    return summary_str

async def process_folder(path, dirpath, dirname, pbar, instructions, unique_id):
    subdir_path = os.path.join(dirpath, dirname)
    if subdir_path != path:
        pbar.update(1)
    subdir_folder_summary = await process_directory(subdir_path, pbar, instructions, unique_id)
    return {"name": dirname, "summary": subdir_folder_summary}

async def process_directory(path, pbar, instructions='', unique_id=''):

    if unique_id == '':
        letters = string.ascii_letters
        unique_id = ''.join(random.choice(letters) for _ in range(7))

    if instructions != '':
        instructions = f"{instructions}\n\n"
    
    doc_summaries, folder_summaries = [], []

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        if f'00. Folder contents {unique_id}.xlsx' in filenames:
            continue

        filenames = [f for f in filenames if any(f.endswith(ft) for ft in accepted_filetypes) and not f.startswith('~$')]

        # Process documents in the current directory
        file_tasks = [process_doc({"name": filename, "path": os.path.join(dirpath, filename), "parent": dirpath}, instructions, pbar) for filename in filenames]
        # Run tasks in parallel and wait for all to complete
        doc_summaries = [{"name": filename, "summary": summary} for filename, summary in zip(filenames, await asyncio.gather(*file_tasks))]
                
        # folders
        folder_tasks = [process_folder(path, dirpath, dirname, pbar, instructions, unique_id) for dirname in dirnames]
        folder_summaries = await asyncio.gather(*folder_tasks)       
        
        folder_sum = await get_folder_sum(doc_summaries, instructions)
        await create_folder_table(dirpath, doc_summaries, folder_summaries, unique_id)
        doc_summaries, folder_summaries = [], []

    return folder_sum

def count_items(INDEX_PATH):
    total_items = 0
    for dirpath, dirnames, filenames in os.walk(INDEX_PATH):
        # Filter out filenames by accepted filetypes
        filenames = [f for f in filenames if any(f.endswith(ft) for ft in accepted_filetypes)]
        total_items += len(filenames)
        total_items += len(dirnames)
    return total_items
