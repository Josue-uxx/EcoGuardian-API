import random

water_tips = [
    "Cierra el grifo mientras te cepillas los dientes.",
    "Repara fugas de agua en casa.",
    "Utiliza una cubeta para lavar el automóvil."
]

energy_tips = [
    "Apaga las luces cuando no las uses.",
    "Desconecta cargadores que no estén en uso.",
    "Utiliza bombillas LED."
]

recycling_tips = [
    "Separa plástico, papel y vidrio.",
    "Lava los envases antes de reciclarlos.",
    "No mezcles residuos orgánicos con reciclables."
]

compost_tips = [
    "Agrega cáscaras de frutas al compost.",
    "Mezcla residuos húmedos y secos.",
    "Evita colocar plástico en el compost."
]

def get_home_tip(category):

    if category == "water":
        return random.choice(water_tips)

    elif category == "energy":
        return random.choice(energy_tips)

    elif category == "recycling":
        return random.choice(recycling_tips)

    elif category == "compost":
        return random.choice(compost_tips)

    return "No hay consejos disponibles."