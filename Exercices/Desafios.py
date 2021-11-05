# Desafio dos contadores (0 a 8 & 10 a 2) - ao mesmo tempo)

# for v1, v2 in enumerate(range(10, 1, -1)):
#   print(v1, v2)


# Desafio Valide um CPF - 16899535009
'''
while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]

    reverse = 10  # Contador reverso
    total = 0

    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9
            index -= 9  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverse  # Valor total da multiplicação

        reverse -= 1  # Decrementa o contador reverso
        if reverse < 2:
            reverse = 11
            digit = 11 - (total % 11)

            if digit > 9:  # Se o digito for > que 9 o valor é 0 (Algoritmo)
                digit = 0
            total = 0
            novo_cpf += str(digit)  # Concatena o digito gerado no novo cpf

    sequencia = novo_cpf == str(novo_cpf[0] * len(cpf))   #Evita sequências

    if cpf == novo_cpf:
        print(f"Válido - {novo_cpf}")
    else:
        print(f"Inválido - {novo_cpf}")
'''


# Desafio GERADOR DE CPF
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
reverse = 10                          # Contador reverso
total = 0

for index in range(19):
    if index > 8:                     # Primeiro índice vai de 0 a 9
        index -= 9                    # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverse  # Valor total da multiplicação

    reverse -= 1                      # Decrementa o contador reverso
    if reverse < 2:
        reverse = 11
        digit = 11 - (total % 11)

        if digit > 9:  # Se o digito for > que 9 o valor é 0 (Algoritmo)
            digit = 0
        total = 0
        # Concatena o digito gerado no novo cpf
        novo_cpf += str(digit)

print(novo_cpf)
