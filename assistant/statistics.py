from assistant.ecoscore import calculate_score, get_level

def get_statistics():

    stats = calculate_score()

    level = get_level(stats["score"])

    return {
        "total": stats["total"],
        "recyclables": stats["recyclables"],
        "compostables": stats["compostables"],
        "score": stats["score"],
        "level": level
    }