"""
1 -
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
'''
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def find_duplicate1(param_list_inteiros):
    num_check = set()
    duplicate1 = -1

    for number in param_list_inteiros:
        if number in num_check:
            duplicate1 = number
            break
        num_check.add(number)
    return duplicate1


for list_inteiros in lista_de_listas_de_inteiros:
    print(
        f'List = {list_inteiros} | Duplicate Number = {find_duplicate1(list_inteiros)}')
'''
#----------------------------------------------------------------------------------------------------------#


# 2 -
'''
numbers = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
numb = 10
list1 = [numbers[i:i + numb] for i in range(0, len(numbers), numb)]
return1 = '.'.join(list1)
print(list1)
print(return1)
'''
#----------------------------------------------------------------------------------------------------------#

#03 - 
''''
cart = []

cart.append(('Product1', 30))
cart.append(('Product2', 20))
cart.append(('Product3', 50))
cart.append(('Product4', 40))

totalv = sum([float(y) for x,y in cart])
print(f'You have to pay ${totalv}')



# My solution 
for product in cart:
    totalv.append(product[1])
finalv = (sum(totalv))
print(f'You have to pay ${finalv}')
'''
#----------------------------------------------------------------------------------------------------------#

#04 - 
#Sistema de desconto possível.
from itertools import zip_longest

list_a = [1,2,3,4,10,12,14]
list_b = [1,2,3,4]

list_sum = [x+y for x,y in zip_longest(list_a, list_b, fillvalue= 0)]
print(list_sum)


'''
Res 2
for i, _ in enumerate(list_b):
    list_sum.append(list_a[i]+list_b[i])
print(list_sum)
'''

'''
Res 1
for i in range(len(list_b)):
    list_sum.append(list_a[i]+list_b[i])
print(list_sum)
'''

#----------------------------------------------------------------------------------------------------------#