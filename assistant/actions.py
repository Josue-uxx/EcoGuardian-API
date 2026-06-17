try:
    from assistant.chat_window import open_chat_window
except:
    def open_chat_window():
        pass

try:
    from assistant.home_window import open_home_window
except:
    def open_home_window():
        pass

try:
    from assistant.goals_window import open_goals_window
except:
    def open_goals_window():
        pass

from assistant.ecotips import get_tip
from assistant.recycling_guide import get_recycling_guide
from assistant.compost_guide import get_compost_guide

from assistant.ecoscore import calculate_score
from assistant.ecoscore import get_level

from assistant.report import generate_report
from assistant.statistics import get_statistics
from assistant.charts import generate_chart
from assistant.achievements import get_achievements

import subprocess
import sys


def open_camera():
    subprocess.Popen(
        [sys.executable, "-m", "vision.detector"]
    )


def open_chat():
    open_chat_window()


def open_home():
    open_home_window()


def open_goals():
    open_goals_window()


def get_score_data():

    stats = calculate_score()

    return {
        "total": stats["total"],
        "recyclables": stats["recyclables"],
        "compostables": stats["compostables"],
        "score": stats["score"],
        "level": get_level(stats["score"])
    }


def get_report():
    return generate_report()


def get_chart():
    return generate_chart()


def get_achievements_data():
    return get_achievements()


def get_statistics_data():
    return get_statistics()
