import json

from assistant.statistics import get_statistics

GOAL_FILE = "data/goals.json"


def get_goal():

    try:

        with open(
            GOAL_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            return data["goal"]

    except:

        return 20


def set_goal(goal):

    with open(
        GOAL_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {"goal": goal},
            file,
            indent=4
        )


def get_progress():

    stats = get_statistics()

    goal = get_goal()

    current = stats["recyclables"]

    percentage = min(
        round((current / goal) * 100, 2),
        100
    )

    completed = current >= goal

    return {
        "goal": goal,
        "current": current,
        "percentage": percentage,
        "completed": completed
    }