"""
Manages file operations like reading and writing JSON/CSV data.
Example: read_json(file_path) or write_json(file_path, data).
"""
import json
import os


def read_json(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as expenses_file:
            expenses = json.load(expenses_file)
            return expenses
    except FileNotFoundError as e:
        print(f"file not found - {e}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON data - {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return {}

def write_json(file_path, data):
    data_dir = os.path.exists(file_path)
    if not os.path.exists(file_path):
        os.makedirs(data_dir, exist_ok=True)

    with open(file_path, 'w') as expenses_file:
        json.dump(data, expenses_file, indent=4)