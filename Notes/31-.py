'''
# Aula 31 e 32
Formatação de valores com modificadores:
:s - Texto(strings)
:d - Inteiros(int)
:f - Números de ponto flutuante (float)
:. (NUMERO)f - Quantidade de casas decimais (float) = :.2f
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f) = 

> - Esquerda
< - Direita
^  - Centro

num_1 = 1
print(f'{num_1:0>10}')  # 000000001

num_2 = 1150
print(f'{num_2:0<10}')  # 1150000000
print(f'{num_2:.2f}')  # 1150.00

num_3 = 13
print(f'{num_3:0^6}')  # 001300

nome_1 = 'Gustavo'
print(f'{nome_1:#^13}')  # --'###Gustavo###'

nome_2 = 'Yasmim'
nome_formatado = '{:@^10}'.format(nome_2)
print(nome_formatado)  # @@Yasmim@@

nome_3 = 'MaRiA FeRnAnDa'
print(nome_3.title())  # Primeiras letras maiusculas
'''
# Aula 33 - Manipulando Strings
'''
texto = 'GUSTAVO'  # 7 LETRAS - 0123456 - Indices (Espaços contam)
print(texto[2])

url = 'www.google.com.br/'  # -[19 to 1]
print(url[:-1])  # Remoção de um caractere

# Fatiamento da str, selecionando só as que estarão dentro do range
new_string1 = texto[0:3]
new_string2 = url[0::2]  # Pula de uma em uma letra da str
print(new_string1)
print(new_string2)
'''
# Aula 34 - While
x = 0
'''
while x <= 10:
    #continue - Pula para o próximo while
    #break - Finaliza o while
    print(x)
    x = x + 1
'''
'''
x = 0  # coluna

while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1  # x = x + 1
# Pequenos loops em que 
print('Acabou')
'''
# Calculadora Básica
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    op = input('Digite um operador (+, -, /, *): ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if op == '+':
        print(num_1 + num_2)
    elif op == '-':
        print(num_1 - num_2)
    elif op == '/':
        print(num_1 / num_2)
    elif op == '*':
        print(num_1 * num_2)
    else:
        print('O operador não segue os requisitos do sistema.')

    brk = input('Deseja sair da calculadora? [y]es or [n]o: ')

    if brk == 'y':
        break
