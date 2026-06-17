import tkinter as tk
from assistant.chatbot import ask

def open_chat_window():

    window = tk.Toplevel()

    window.title("Chat Ecológico")
    window.geometry("600x400")

    # Área de conversación
    chat_area = tk.Text(
        window,
        height=15,
        width=70
    )

    chat_area.pack(pady=10)

    # Entrada de texto
    entry = tk.Entry(
        window,
        width=50
    )

    entry.pack(side="left", padx=10, pady=10)

    def send_message():

        question = entry.get()

        if not question:
            return

        answer = ask(question)

        chat_area.insert(
            tk.END,
            f"\nUsuario: {question}\n"
        )

        chat_area.insert(
            tk.END,
            f"EcoGuardian: {answer}\n"
        )

        entry.delete(0, tk.END)

    send_button = tk.Button(
        window,
        text="Enviar",
        command=send_message
    )

    send_button.pack(side="left")

    window.mainloop()