import random

tips = [
    "Usa botellas reutilizables para reducir residuos.",
    "Separa los residuos orgánicos de los reciclables.",
    "Apaga las luces cuando no las necesites.",
    "Reduce el uso de bolsas plásticas.",
    "Composta restos de frutas y verduras.",
    "Recicla papel y cartón limpios.",
    "Ahorra agua cerrando el grifo mientras te cepillas los dientes."
]

def get_tip():
    return random.choice(tips)