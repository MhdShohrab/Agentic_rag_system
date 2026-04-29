# backend/memory/memory_store.py
import json
# File path (inside backend folder)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "memory.json")


# LOAD MEMORY FILE
def _load_memory_file():
    # If file does not exist → return empty memory
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        #Try reading JSON data
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:                   #Corrupted JSON  or empty json    → safe (ignore & reset)
        return {}


# SAVE MEMORY FILE
def _save_memory_file(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


# GET MEMORY
def get_memory(user_id):
    data = _load_memory_file()

    if user_id not in data:
        data[user_id] = {
            "summary": "",
            "recent": []
        }
        _save_memory_file(data)

    return data[user_id]


# SAVE MEMORY
def save_memory(user_id, memory):
    data = _load_memory_file()
    data[user_id] = memory
    _save_memory_file(data)