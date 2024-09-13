import os 
os.system("cls|| clear")
"""
crie um algoritmo que possa receba do usuario valores e armazene
 em um vetor 5 numeros, caso seja informado um negativo, atribua valor 0
"""


QUANTIDADEDENUMEROS = 5

numero = []
for i in range(QUANTIDADEDENUMEROS): 
 numeros = int(input("Digite um numero: "))
 
 if numeros < 0 :
  numeros = 0
 numero.append(numeros)
for contador, numeros3 in enumerate(numero):
 print(f"{contador + 1} numero {numeros3}")