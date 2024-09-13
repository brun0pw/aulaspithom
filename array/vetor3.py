import os
os.system("cls || clear")
numeros = []

for i in range (5):
    numero = int(input("digite um numero: "))
    numeros.append(numero)
menor = min(numeros)
maior = max(numeros)
print(f"você digitou {numeros}, o maior número foi {maior} , e o menor número foi {menor}")