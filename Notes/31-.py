'''
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
