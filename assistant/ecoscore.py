import json

def calculate_score():

    with open("data/history.json", "r", encoding="utf-8") as file:
        history = json.load(file)

    total = len(history)

    reciclables = sum(
        1 for item in history
        if item["recyclable"]
    )

    compostables = sum(
        1 for item in history
        if item["compostable"]
    )

    score = reciclables * 2 + compostables

    return {
        "total": total,
        "recyclables": reciclables,
        "compostables": compostables,
        "score": score
    }

def get_level(score):

    if score >= 100:
        return "🏆 EcoHéroe"

    elif score >= 50:
        return "🌍 EcoExperto"

    elif score >= 20:
        return "♻️ EcoAprendiz"

    else:
        return "🌱 Principiante"