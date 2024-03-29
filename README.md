# academicAI

Open source AI-powered tools for academic research

---

## Information

Contained within this repository is a number of tools, utilising generative AI,
which can be used for academic purposes.

The main interface for each tool is the respective Jupyter notebook. These
notebooks interface with respective folders that contain feature logic.

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
