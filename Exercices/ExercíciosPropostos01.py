'''
Exercícios Propostos 01

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
'''
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
'''
''' 
Exercícios Propostos 02
A) Crie uma função que exibe uma saudação com os parâmetros saudação e nome

B) Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles

C) Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex: 10%).
Retorne (return) o valor do primeiro número somado o aumento do percentual do mesmo.

D) Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da função
for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e 3, retorne Fizz Buzz,
caso contrário, retorne o número enviado.

'''
# RESPOSTAS:

# A) :


def saudacao(msg, name):
    print(f'{msg} {name}!')


saudacao('Hey', 'Gus')


def soma(n1, n2, n3):
    print(n1+n2+n3)


soma(1, 2, 3)


def num(n1, n2):
    return (n1 * (n2/100))


v1 = int(input('Insira o 1° valor: '))
v2 = int(input('Insira o 2° valor: '))

prc = num(v1, v2)
if prc:
    print(f'Valor ganho: {prc} - Saldo: {prc+v1}')
else:
    print('Conta inválida.')

if (prc % 3 == 0):
    print('Fizz')
elif (prc % 5 == 0):
    print('Buzz')
elif (prc % 3 == 0 and prc % 5 == 0):
    print('FizzBuzz')
else:
    print(f'Nenhum dos dois! {prc}')
