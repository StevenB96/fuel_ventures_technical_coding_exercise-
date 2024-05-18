import json
import os

def load_json_file():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, '../snomed_codes.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data