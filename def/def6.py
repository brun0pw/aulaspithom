import os
os.system("cls || clear")


def impar ():  
  
    pares = 0
    impares = 0

    
    for i in range(6):
     numero = int(input("Digite um número: "))
     if numero % 2 == 0:
        pares += 1
     else: 
        impares += 1
    print(f"Quantos números são pares: {pares}")
    print(f"Quantos números são pares: {impares}")
 



impar()

