import tkinter as tk
from tkinter import messagebox


def avaliar_1ounenhum(numero):
    if numero == 1:
        return "É 1."
    else:
        return "Não é 1."


def verificar_numero():
    try:
        numero = int(entry_numero.get())
        resposta = avaliar_1ounenhum(numero)
        label_resultado.config(text=resposta)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido, vagabundo!")


# Criando a janela principal
janela = tk.Tk()
janela.title("Verificador de Número")
janela.geometry("300x200")

# Label para instruções
label_instrucoes = tk.Label(janela, text="Digite um número e clique em 'Verificar':")
label_instrucoes.pack(pady=10)

# Campo de entrada para o número
entry_numero = tk.Entry(janela, width=15)
entry_numero.pack(pady=5)

# Botão para verificar o número
botao_verificar = tk.Button(janela, text="Verificar", command=verificar_numero)
botao_verificar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Executa a janela
janela.mainloop()
