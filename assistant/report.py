from datetime import datetime
from assistant.ecoscore import calculate_score, get_level
import os

def generate_report():

    stats = calculate_score()

    level = get_level(stats["score"])

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    os.makedirs("reportes", exist_ok=True)

    filename = f"reportes/reporte_{fecha}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("========== REPORTE ECOGUARDIAN AI ==========\n\n")

        file.write(f"Fecha: {fecha}\n\n")

        file.write(f"Objetos detectados: {stats['total']}\n")
        file.write(f"Reciclables: {stats['recyclables']}\n")
        file.write(f"Compostables: {stats['compostables']}\n")
        file.write(f"EcoScore: {stats['score']}\n")
        file.write(f"Nivel: {level}\n")

        file.write("\n===========================================\n")

    return filename