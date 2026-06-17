import tkinter as tk
from tkinter import messagebox

from assistant.reminders import (
    add_reminder,
    get_reminders,
    delete_reminder
)


def open_reminder_window():

    window = tk.Toplevel()

    window.title("Recordatorios")
    window.geometry("550x500")

    tk.Label(
        window,
        text="⏰ Recordatorios",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # -------------------------
    # Descripción
    # -------------------------

    tk.Label(
        window,
        text="Descripción"
    ).pack()

    entry_text = tk.Entry(
        window,
        width=40
    )

    entry_text.pack(pady=5)

    # -------------------------
    # Fecha
    # -------------------------

    tk.Label(
        window,
        text="Fecha (DD/MM/AAAA)"
    ).pack()

    entry_date = tk.Entry(
        window,
        width=40
    )

    entry_date.pack(pady=5)

    # -------------------------
    # Hora
    # -------------------------

    tk.Label(
        window,
        text="Hora (HH:MM)"
    ).pack()

    entry_time = tk.Entry(
        window,
        width=40
    )

    entry_time.pack(pady=5)

    # -------------------------
    # Lista
    # -------------------------

    listbox = tk.Listbox(
        window,
        width=70,
        height=12
    )

    listbox.pack(pady=10)

    # -------------------------
    # Actualizar lista
    # -------------------------

    def refresh():

        listbox.delete(0, tk.END)

        reminders = get_reminders()

        for reminder in reminders:

            if isinstance(reminder, str):

                listbox.insert(
                    tk.END,
                    reminder
                )

            else:

                texto = (
                    f"{reminder['text']} | "
                    f"{reminder['date']} | "
                    f"{reminder['time']}"
                )

                listbox.insert(
                    tk.END,
                    texto
                )

    # -------------------------
    # Agregar
    # -------------------------

    def add():

        text = entry_text.get().strip()
        date = entry_date.get().strip()
        time = entry_time.get().strip()

        if not text or not date or not time:

            messagebox.showwarning(
                "Aviso",
                "Completa todos los campos."
            )
            return

        add_reminder(
            text,
            date,
            time
        )

        entry_text.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_time.delete(0, tk.END)

        refresh()

    # -------------------------
    # Eliminar
    # -------------------------

    def remove():

        selected = listbox.curselection()

        if not selected:

            messagebox.showwarning(
                "Aviso",
                "Selecciona un recordatorio."
            )
            return

        index = selected[0]

        delete_reminder(index)

        refresh()

    # -------------------------
    # Botones
    # -------------------------

    tk.Button(
        window,
        text="Agregar",
        command=add
    ).pack(pady=5)

    tk.Button(
        window,
        text="Eliminar seleccionado",
        command=remove
    ).pack(pady=5)

    refresh()