import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from client import client, dalle_model
import json
import time
import requests

def gen_image(prompt, dim):    
    dimensions = "1024x1024"
    if dim.lower() == "wide":
        dimensions = '1792x1024'
    elif dim.lower() == "tall":
        dimensions = '1024x1792'

    response = client.images.generate(
        model=dalle_model,
        prompt=prompt,
        quality="hd",
        n=1,
        size=dimensions
    )

    url = response.data[0].url

    if not os.path.exists('generated images'):
        os.makedirs('generated images')
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f"generated images/{timestamp}.png"

    with open(filename, 'wb') as f:
        f.write(requests.get(url).content)

    json_filename = "generated images/00. generated images.json"

    if not os.path.exists(json_filename):
        with open(json_filename, 'w') as f:
            f.write('[]')

    # Load existing data
    with open(json_filename, 'r') as f:
        try:
            data = json.load(f)
            # Ensure data is a list
            if not isinstance(data, list):
                data = [data]
        except json.JSONDecodeError:
            data = []

    # Append new data
    data.append({'prompt': prompt,
                'actual_description': response.data[0].revised_prompt,
                 'filename': filename,
                 'url': url,
                 'dimensions': dimensions})

    # Write updated data
    with open(json_filename, 'w') as f:
        json.dump(data, f)

    return filename
