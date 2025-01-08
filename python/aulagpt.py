try:

    num1=float(input('Digite o primeiro número: '))
    num2=float(input('Digite o segundo número: '))

    operacao = input('Escolha a operação (+, -, *, /): ')

    if operacao == '+':
        resultado = num1 + num2

    elif operacao == '-':
        resultado = num1 - num2

    elif operacao == '*':
        resultado = num1 * num2

    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = 'Erro: Divisão por zero não é permitida.'
    else:
        resultado = 'Operação inválida.'

    print('O resultado é:', resultado)
except ValueError:
    print('Erro: Por favor, insira apenas números válidos.')