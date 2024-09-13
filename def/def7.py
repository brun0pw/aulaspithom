import os
os.system("cls || clear")

def contar_pares_e_impares(numeros):
    pares = 0
    impares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Quantos números são pares: {pares}")
    print(f"Quantos números são ímpares: {impares}")
    return pares, impares


numeros = []


for i in range(6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)


pares, impares = contar_pares_e_impares(numeros)