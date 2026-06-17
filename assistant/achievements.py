from assistant.statistics import get_statistics

def get_achievements():

    stats = get_statistics()

    logros = []

    if stats["recyclables"] >= 1:
        logros.append("✓ Primer Reciclaje")

    if stats["score"] >= 20:
        logros.append("✓ ♻️ EcoAprendiz")

    if stats["score"] >= 50:
        logros.append("✓ 🌍 EcoExperto")

    if stats["score"] >= 100:
        logros.append("✓ 🏆 EcoHéroe")

    if stats["total"] >= 100:
        logros.append("✓ 📸 100 Objetos Detectados")

    if not logros:
        logros.append("Aún no has desbloqueado logros.")

    return "\n".join(logros)