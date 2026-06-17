import tkinter as tk
from tkinter import messagebox

from assistant.goals import (
    get_goal,
    set_goal,
    get_progress
)


def open_goals_window():

    window = tk.Toplevel()

    window.title("Metas Ecológicas")
    window.geometry("500x400")

    tk.Label(
        window,
        text="🎯 Metas Ecológicas",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    goal_entry = tk.Entry(
        window,
        width=20
    )

    goal_entry.pack(pady=5)

    result_label = tk.Label(
        window,
        text="",
        font=("Arial", 11)
    )

    result_label.pack(pady=20)

    def update_view():

        progress = get_progress()

        text = (
            f"Meta: {progress['goal']} reciclables\n\n"
            f"Progreso: {progress['current']} / {progress['goal']}\n\n"
            f"{progress['percentage']}% completado"
        )

        if progress["completed"]:

            text += "\n\n🎉 ¡Meta completada!"

        result_label.config(text=text)

    def save_goal():

        try:

            goal = int(goal_entry.get())

            if goal <= 0:
                raise ValueError

            set_goal(goal)

            update_view()

            messagebox.showinfo(
                "EcoGuardian",
                "Meta guardada correctamente"
            )

        except:

            messagebox.showerror(
                "Error",
                "Ingresa un número válido"
            )

    tk.Button(
        window,
        text="Guardar Meta",
        command=save_goal
    ).pack(pady=5)

    update_view()