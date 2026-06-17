import json

def show_history():

    with open("data/history.json", "r", encoding="utf-8") as file:
        history = json.load(file)

    if not history:
        print("\nNo hay registros.")
        return

    print("\n===== Historial =====")

    for i, item in enumerate(history, start=1):

        print(
            f"{i}. {item['object']} | "
            f"Reciclable: {item['recyclable']} | "
            f"Compostable: {item['compostable']}"
        )