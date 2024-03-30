from openai import OpenAI, AzureOpenAI
from config import AZURE_OPENAI_KEY, AZURE_OPENAI_BASE_URL, OPEN_AI_KEY

client = None

if (AZURE_OPENAI_KEY and AZURE_OPENAI_BASE_URL):
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        api_version="2024-02-15-preview",
        azure_endpoint=AZURE_OPENAI_BASE_URL,
        max_retries=10) 
else:
    client = OpenAI(
        api_key=OPEN_AI_KEY, max_retries=9)