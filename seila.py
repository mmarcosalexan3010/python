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

# Solicitando idade, peso e altura da pessoa
try:
    idade = int(input("Qual é a sua idade? "))
    peso = float(input("Qual é o seu peso em kg? "))
    altura = float(input("Qual é a sua altura em metros (ex: 1.75)? "))
    resposta = avaliar_saude(idade, peso, altura)
    print(resposta)
except ValueError:
    print("Por favor, insira valores válidos para idade, peso e altura.")
    