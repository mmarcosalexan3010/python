import tkinter as tk
from tkinter import messagebox


def avaliar_saude(idade, peso, altura):
    # Avaliação baseada em idade, peso e altura
    if 10 <= idade <= 14:
        if 50 <= peso <= 55 and 1.40 <= altura <= 1.60:
            return "Seu peso e altura estão dentro da faixa saudável para sua idade (10 a 14 anos)."
        elif peso < 50 or altura < 1.40:
            return "Você está abaixo do peso ou altura saudável para sua idade (10 a 14 anos)."
        elif peso > 55 or altura > 1.60:
            return "Você está acima do peso ou altura saudável para sua idade (10 a 14 anos)."
    elif 15 <= idade <= 19:
        if 60 <= peso <= 70 and 1.60 <= altura <= 1.80:
            return "Seu peso e altura estão dentro da faixa saudável para sua idade (15 a 19 anos)."
        elif peso < 60 or altura < 1.60:
            return "Você está abaixo do peso ou altura saudável para sua idade (15 a 19 anos)."
        elif peso > 70 or altura > 1.80:
            return "Você está acima do peso ou altura saudável para sua idade (15 a 19 anos)."
    elif 20 <= idade <= 30:
        if 65 <= peso <= 80 and 1.60 <= altura <= 1.85:
            return "Seu peso e altura estão dentro da faixa saudável para sua idade (20 a 30 anos)."
        elif peso < 65 or altura < 1.60:
            return "Você está abaixo do peso ou altura saudável para sua idade (20 a 30 anos)."
        elif peso > 80 or altura > 1.85:
            return "Você está acima do peso ou altura saudável para sua idade (20 a 30 anos)."
    elif 31 <= idade <= 45:
        if 70 <= peso <= 85 and 1.60 <= altura <= 1.85:
            return "Seu peso e altura estão dentro da faixa saudável para sua idade (31 a 45 anos)."
        elif peso < 70 or altura < 1.60:
            return "Você está abaixo do peso ou altura saudável para sua idade (31 a 45 anos)."
        elif peso > 85 or altura > 1.85:
            return "Você está acima do peso ou altura saudável para sua idade (31 a 45 anos)."
    elif 46 <= idade <= 60:
        if 70 <= peso <= 90 and 1.60 <= altura <= 1.85:
            return "Seu peso e altura estão dentro da faixa saudável para sua idade (46 a 60 anos)."
        elif peso < 70 or altura < 1.60:
            return "Você está abaixo do peso ou altura saudável para sua idade (46 a 60 anos)."
        elif peso > 90 or altura > 1.85:
            return "Você está acima do peso ou altura saudável para sua idade (46 a 60 anos)."
    else:
        return "Não temos dados para essa faixa etária."


def avaliar():
    try:
        idade = int(entry_idade.get())
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        resultado = avaliar_saude(idade, peso, altura)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para idade, peso e altura.")


# Criando a interface com tkinter
janela = tk.Tk()
janela.title("Avaliador de Saúde")
janela.geometry("300x300")

# Labels e entradas
tk.Label(janela, text="Idade:").pack(pady=5)
entry_idade = tk.Entry(janela)
entry_idade.pack(pady=5)

tk.Label(janela, text="Peso (kg):").pack(pady=5)
entry_peso = tk.Entry(janela)
entry_peso.pack(pady=5)

tk.Label(janela, text="Altura (m):").pack(pady=5)
entry_altura = tk.Entry(janela)
entry_altura.pack(pady=5)

# Botão para avaliar
btn_avaliar = tk.Button(janela, text="Avaliar Saúde", command=avaliar)
btn_avaliar.pack(pady=20)

# Rodando o loop principal
janela.mainloop()
