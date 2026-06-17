import matplotlib.pyplot as plt

from assistant.statistics import get_statistics

def generate_chart():

    stats = get_statistics()

    reciclables = stats["recyclables"]
    compostables = stats["compostables"]
    no_reciclables = stats["total"] - reciclables

    categorias = [
        "Reciclables",
        "Compostables",
        "No reciclables"
    ]

    valores = [
        reciclables,
        compostables,
        no_reciclables
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(categorias, valores)

    plt.title("EcoGuardian AI - Estadísticas")
    plt.ylabel("Cantidad")

    plt.show()