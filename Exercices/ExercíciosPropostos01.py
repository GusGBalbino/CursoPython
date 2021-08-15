'''
A) Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.


B) Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.


C) Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos, escreva: 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva: "Seu nome é normal"; maior que 6 letras
escreva: 'Seu nome é grande'.
'''

# RESPOSTAS:
# A)

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é ímpar.')
else:
    print('Isso não é um número inteiro.')


# B)

hora = input('Digite o horário. (00 - 23h) ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Por favor digite um horário entre 00 e 23h.')
    else:
        if hora <= 11:
            print(f'{hora}h - BOM DIA!')
        elif hora <= 17:
            print(f'{hora}h - BOA TARDE!')
        else:
            print(f'{hora}h - BOA NOITE!')


# C)

nome = input('Digite seu nome de usuário: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'Seu nome é curto, {tamanho} letras totais.')
elif tamanho == 5 or tamanho == 6:
    print(f'Seu nome é normal, {tamanho} letras totais.')
else:
    print(f'Seu nome é grande, {tamanho} letras totais.')
