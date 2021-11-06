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


def divisao(n1, n2):
    if n2 <= 0:
        return
    return n1 / n2


div = divisao(8, 1)
if div:
    print(div)
else:
    print('Conta inválida.')
