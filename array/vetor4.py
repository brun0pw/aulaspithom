import os
os.system("cls || clear")
numeros = []

impar = 0
par = 0

for i in range (6):
    numero = int(input("digite um numero: "))
    numeros.append(numero)
    if numero % 2 == 0:
        impar += 1
    else: 
        par += 1

print(f"os números ímpar foram {impar}\n e os números pares foram {par}")