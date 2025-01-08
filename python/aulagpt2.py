try:
    
    entrada=input('Digite os números separados por vírgula: ')

    if not entrada.strip():
        print('Erro: A lista de números está vazia.')
    else:

        numeros=[float(num) for num in entrada.split(',')]

        soma=sum(numeros)
        media=soma/len(numeros)

        print(f'soma: {soma:.2f}')
        print(f'media: {media:.2f}')

except ValueError:
    print('Erro: Por favor, insira apenas números válidos.')