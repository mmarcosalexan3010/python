import tkinter as tk

def show_message():
    label.config(text="Olá, Mundo!")

# Cria a janela principal
root = tk.Tk()
root.title("Minha GUI")

# Adiciona um botão e um rótulo
button = tk.Button(root, text="Clique aqui", command=show_message)
button.pack()

label = tk.Label(root, text="")
label.pack()

# Inicia o loop da interface
root.mainloop()
