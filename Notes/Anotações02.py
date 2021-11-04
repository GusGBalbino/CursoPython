'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''
'''
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[1:4])  # Vai do ind 1 ao 4
print(lista[:3])   # Para até o ind 3
print(lista[2:])   # Vai do ind até o fim
print(lista[::2])  # Pula de 2 em 2


l1 = [1, 2, 3, 4, 5, 6]
l2 = list(range(1, 11))  # Range pra fazer lista
'''
# l1.extend(l2)      Adiciona l2 a l1
# l2.append('b')     Adiciona o valor na lista
# l2.insert(0,'lol') Adiciona o valor ao indice da lista
# l2.pop(0)          Excluir um valor específico
# del(l2[3:5])       Excluir os valores no range 3 a 5
# print(max(l2))     Maior valor da lista
# print(min(l2))     Menor valor da lista

'''
secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ei! Digite apenas uma letra!')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" NÃO existe na palavra secreta.')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    if secreto_temp == secreto:
        print(f'YOU WIN! A palavra era {secreto_temp}')
        break
    else:
        print(f'Palavra: {secreto_temp}')
'''

# Funções de split, join e enumerate

string = 'A lâmina que não se vê, é a mais mortífera.'
lista = string.split(' ')
string2 = ','.join(lista)

print(lista)
print(string2)

for v1, v2 in enumerate(lista):
    print(v1, v2)
# v1: indice v2: valor
