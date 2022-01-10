# def in Python
'''
def saudacao(msg = "Olá", nome):
    print(msg, nome)

name = input('Digite seu nome de usuário: ')

if (name == " "):
    print("Digite um nome de usuário.")
else:
    saudacao(msg, f"{name}!")
'''

'''
def divisao(n1, n2):
    if n2 <= 0:
        return
    return n1 / n2


div = divisao(8, 1)
if div:
    print(div)
else:
    print('Conta inválida.')
'''

# *args e #kwargs (podem ser o que quiser -usados por convenção)

''' #ARGS AND KWARGS
def function(*args, **kwargs):
    print(args)
    # print(kwargs)
    #print(kwargs['nome'], kwargs['sb'])

    nome = kwargs.get('nome')
    sb = kwargs.get('sb')
    print(nome, sb)


lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
function(*lista, *lista2, nome='Gustavo', sb='Gomes')
'''
''' #LAMBDA - 
lista = [
    ["P1", 13],
    ["P2", 5],
    ["P3", 42],
    ["P4", 25],
    ["P5", 60],
]

print(sorted(lista, key=lambda item: item[1]))
print(lista)
'''
'''
# TUPLES

t1 = 1, 2, 3, "a", "Gus"
print(t1)
t1 = list(t1)
t1[3] = "Gomes"
print(t1)
'''
