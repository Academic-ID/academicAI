import os 
# EXAMPLE CONFIG FILE
# This file contains the necessary configuration values use throughout the tools.
# You can set the values as environmentals variables or define them directly in this file (to do so, remove the os.getenv('XYZ...') and replace with the value, such as: 'sk_12345567dsbhfidsuibdfsd').

# OPENAI CONFIG
# You can chose to use either Azure's OpenAI service OR directly call OpenAI's API. 
# If you are using Azure, you need to provide the Azure key and base URL. If you are using OpenAI, you only need to provide your API key.
# AZURE OPENAI 
AZURE_OPENAI_KEY=os.getenv('AZURE_OPENAI_KEY')
# base url will look like: 'https://{resource-name}.openai.azure.com'
AZURE_OPENAI_BASE_URL=os.getenv('AZURE_OPENAI_BASE_URL')
# OPENAI
OPEN_AI_KEY=os.getenv('OPEN_AI_KEY')
# The default model needs to be updated based on your choice of Azure vs OpenAI. 
# If using Azure, this is the DEPLOYMENT name. 
# Do not set this as a GPT4 vision deployment as the code base requires function calls. If using OpenAI, the vision model will automatically be selected where needed, if using Azure, set the dedicated vision deployment in the next variable.
# If using OpenAI, use the standard model names they provide (your API key must be able to access them); the current default is "gpt-4-0125-preview".
DEFAULT_MODEL=os.getenv('DEFAULT_MODEL')
# If using Azure, set the deployment name for the vision service here. This needs to be in the same resource as the provided key and base url 
VISION_MODEL=os.getenv('VISION_MODEL')
# If using Azure, set the deployment name for the DALLE service here if you want to use image generation. This needs to be in the same resource as the provided key and base url
DALLE_MODEL=os.getenv('DALLE_MODEL')
# If using Azure, and wanting to transcribe audio, you need to provide the DEPLOYMENT in Azure for the Whispter service, this needs to be in the same resource as the provided key and base url
WHISPER_DEPLOYMENT=os.getenv('WHISPER_DEPLOYMENT')

# ELEVENLABS CONFIG
ELEVEN_API_KEY=os.getenv('ELEVEN_API_KEY')