#save_response.py
import json
import os

# Save response as JSON file
def save_JSON_response(file_name, data):
    file_path = os.path.join('TOC', file_name)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    # print(f"Response saved to {file_path}")

def save_XML_response(file_name, data):
    file_path = os.path.join('Responses', file_name)
    with open(file_path, 'w') as file:
        file.write(data)
    # print(f"Response saved to {file_path}")

def createDirectory():
    os.makedirs('Responses', exist_ok=True)

def get_full_path(file_name):
    file_path = os.path.join('Responses', file_name)
    return file_path

def file_exist(file_path):
    return os.path.isfile(file_path)