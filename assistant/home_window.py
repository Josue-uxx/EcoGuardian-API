import tkinter as tk
from tkinter import messagebox

from assistant.home_assistant import get_home_tip
from assistant.reminder_window import open_reminder_window


def open_home_window():

    window = tk.Toplevel()

    window.title("Asistente del Hogar")
    window.geometry("500x400")

    tk.Label(
        window,
        text="🏠 Asistente del Hogar",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    def show_water():
        messagebox.showinfo(
            "Ahorro de Agua",
            get_home_tip("water")
        )

    def show_energy():
        messagebox.showinfo(
            "Ahorro de Energía",
            get_home_tip("energy")
        )

    def show_recycling():
        messagebox.showinfo(
            "Reciclaje",
            get_home_tip("recycling")
        )

    def show_compost():
        messagebox.showinfo(
            "Compostaje",
            get_home_tip("compost")
        )

    def show_reminders():
        open_reminder_window()

    tk.Button(
        window,
        text="💧 Ahorro de Agua",
        width=30,
        command=show_water
    ).pack(pady=5)

    tk.Button(
        window,
        text="⚡ Ahorro de Energía",
        width=30,
        command=show_energy
    ).pack(pady=5)

    tk.Button(
        window,
        text="♻️ Reciclaje",
        width=30,
        command=show_recycling
    ).pack(pady=5)

    tk.Button(
        window,
        text="🌱 Compostaje",
        width=30,
        command=show_compost
    ).pack(pady=5)

    tk.Button(
        window,
        text="⏰ Recordatorios",
        width=30,
        command=show_reminders
    ).pack(pady=5)