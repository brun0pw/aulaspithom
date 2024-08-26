import os
os.system("cls || clear")
pares = 0
impares = 0

for i in range(5):
  numero = int(input("Digite 1 número: "))
  if numero % 2 == 0:
        pares = pares + 1
  else: 
        impares = impares + 1

print(f"Quantos números são pares: {pares}")
print(f"Quantos números são pares: {impares}")