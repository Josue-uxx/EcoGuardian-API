import json
import os

REMINDER_FILE = "data/reminders.json"


def load_reminders():

    if not os.path.exists(REMINDER_FILE):

        with open(
            REMINDER_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump([], file)

        return []

    try:

        with open(
            REMINDER_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except:

        return []


def save_reminders(reminders):

    with open(
        REMINDER_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            reminders,
            file,
            indent=4,
            ensure_ascii=False
        )


def add_reminder(text, date, time):

    reminders = load_reminders()

    reminders.append(
        {
            "text": text,
            "date": date,
            "time": time
        }
    )

    save_reminders(reminders)


def get_reminders():

    return load_reminders()


def delete_reminder(index):

    reminders = load_reminders()

    if 0 <= index < len(reminders):

        reminders.pop(index)

        save_reminders(reminders)