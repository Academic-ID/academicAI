# academicAI

Open source AI-powered tools for academic research

---

## Information

Contained within this repository is a number of tools, utilising generative AI,
which can be used for academic purposes.

The main interface for each tool is the respective Jupyter notebook. These
notebooks interface with respective folders that contain feature logic.

## Tool list

_The below features can be found at the notebook within the folder corresponding
to the bullet-point's number_

- 01 **Summarise all (supported) files within a folder** (including within
  subdirectories), creating an excel spreadsheet within each folder detailing
  its contents. Great for summarising large volumes of documents.
- 02 **From a list of documents, find relevant pages and return summaries of
  these pages** from a folder of documents (i.e. this tool finds relevant pages
  (from one or many documents) based on a criteria you provide and summarises
  them)
- 03 **Transcribe audio:** use OpenAI's Whisper Large model to convert audio or
  video to text.
- 04 **Miscellaneous:** General AI functions include Chat (using the OpenAI
  Assistants API), image generation (using Dalle3) and text to voice (using
  ElevenLabs)

## Contributing

Interesting in providing additional tools, feel free to make a PR detailing the
feature.

## Setup

1. Clone this repository
2. Update the config.py file with the necessary details (instructions on what is
   needed is contained in that file)
3. [Install Python (we recommended Python 3.12)](https://www.python.org/downloads/)
4. **Create a Virtual Environment:** Run the following command to create a
   virtual environment named venv within your project directory:

   `python3 -m venv venv`

5. Activate the Virtual Environment:

   On Unix-based systems (Linux/MacOS), use the following command:

   `source venv/bin/activate`

   On Windows, the command is slightly different:

   `.\venv\Scripts\activate`

   Once activated, your terminal prompt will usually change to indicate that the
   virtual environment is active. From now on, any Python or Pip commands you
   run will use the versions in the virtual environment, not the global
   versions.

6. Install required packages using:

   `pip install -r requirements.txt`

Once these setup instructions are complete, you should be able to open a
notebook and carry out the logic within. Make sure to select the created `venv`
if prompted to select a kernel.
