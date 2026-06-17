import json

with open("data/materials.json", "r", encoding="utf-8") as file:
    materials = json.load(file)

def ask(question):

    question = question.lower()

    for material, info in materials.items():

        if material.lower() in question:

            reciclable = "Sí" if info["recyclable"] else "No"
            compostable = "Sí" if info["compostable"] else "No"

            return (
                f"\nMaterial: {material}\n"
                f"♻️ Reciclable: {reciclable}\n"
                f"🌱 Compostable: {compostable}\n"
                f"💡 Recomendación: {info['recommendation']}"
            )

    return "No encontré información sobre ese material."