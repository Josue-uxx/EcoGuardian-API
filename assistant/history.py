import json
import os

HISTORY_FILE = "data/history.json"

def save_detection(material, recyclable, compostable):

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = json.load(file)

    history.append({
        "object": material,
        "recyclable": recyclable,
        "compostable": compostable
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)