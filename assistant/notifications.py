from assistant.reminders import get_reminders


def get_next_reminders(limit=3):

    reminders = get_reminders()

    if not reminders:
        return []

    return reminders[:limit]