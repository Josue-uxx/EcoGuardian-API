import json

with open("data/materials.json", "r", encoding="utf-8") as file:
    materials = json.load(file)

def classify(material):

    if material in materials:
        return materials[material]

    return {
        "recyclable": False,
        "compostable": False,
        "recommendation": "Material desconocido."
    }