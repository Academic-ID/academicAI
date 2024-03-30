from openai import OpenAI, AzureOpenAI
from config import AZURE_OPENAI_KEY, AZURE_OPENAI_BASE_URL, OPEN_AI_KEY, DEFAULT_MODEL, VISION_MODEL
import json

client = None

default_model = DEFAULT_MODEL or 'gpt-4-0125-preview'
vision_model = VISION_MODEL or 'gpt-4-vision-preview'

if (AZURE_OPENAI_KEY and AZURE_OPENAI_BASE_URL):
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        api_version="2024-02-15-preview",
        azure_endpoint=AZURE_OPENAI_BASE_URL,
        max_retries=10) 
else:
    client = OpenAI(
        api_key=OPEN_AI_KEY, max_retries=9)
    

# Below are some general functions that can be used across the tools


# Parses the JSON, if an error in JSON parsing, recalls the LLM with the fix json function to get a valid json response.
def parse_JSON(json_str: str):
    """Parses a JSON string returned from an OpenAI function call and returns the JSON object. If there is an error, it will automatically attempt to fix the JSON object."""
    fix_fn = {
      'type': 'function',
      'function': {
        'name': 'fix_object',
        'description':
          'You will be given a JSON Object and a error message. You must fix the JSON object so that it conforms with the error message.',
        'parameters': {
          'type': 'object',
          'properties': {
            'fixedJSON': {
              'type': 'object',
              'description': 'The error free JSON object.',
            },
          },
          'required': ['fixedJSON'],
        },
      },
    }
    try: 
        return json.loads(json_str)
    except Exception as e:        
        print(f'Retrying json: {e}')
        messages = [
      {
        'role': 'system',
        'content':
          'Assistant is a large language model designed to fix and return correct JSON objects.',
      },
      {
        'role': 'user',
        'content': f'ORIGINAL ERROR CONTAINING JSON:\n\n###\n\n{json_str}\n\n###\n\nERROR MESSAGE: {e}',
      },
    ]
        response = client.chat.completions.create(
                    model=DEFAULT_MODEL,
                    messages=messages,                    
                    max_tokens=4096,
                    temperature=0.1,
                    tools=[fix_fn],
                    tool_choice={ 'type': 'function', 'function': { 'name': 'fix_object' } },        
                )        
        try:
            second_test_json = response.choices[0].message.tool_calls[0].function.arguments
            return json.loads(second_test_json)['json_object']
        except:
            raise {'message': 'Failed to successfully parse JSON after two attempts', 'string': json_str}
