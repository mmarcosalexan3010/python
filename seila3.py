def avaliar_1ounenhum(numero):

    if numero == 1:
        return 'É 1.'
    
    else:
        return 'Não é 1.'
    
try:
    numero=int(input('digite um numero: '))
    resposta=avaliar_1ounenhum(numero)
    print(resposta)
except ValueError:
        print('digita algo certo vagabundo')
