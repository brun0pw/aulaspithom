import  os
os.system("cls || clear")

QUANTIDADEDENUMEROS = 5
numeros = []

def numeral():
 contador_de_pares = 0
 contador_de_impares = 0
 contador_de_positivos = 0
 contador_de_negativos = 0
 
 while True:
    for i in range(QUANTIDADEDENUMEROS): 
      numero = int(input(f"Digite o {i + 1}° número: "))
      if numero == 0:
       print("==ERRO==")
       break
      else:
        if numero % 2 == 0:
         contador_de_pares += 1
        if numero % 2 != 0:
         contador_de_impares += 1
        if numero > 0:
         contador_de_positivos += 1
        if numero < 0:
         contador_de_negativos += 1
      numeros.append(numero)
    os.system("cls || clear")
 print(f"A quantidade de numeros foi de {QUANTIDADEDENUMEROS}\nO números positivos foram {contador_de_positivos}")
 print(f"Os números negativos foram {contador_de_negativos}\nOs números pares foram {contador_de_pares}  ")
 print(f"Os números ímpares foram {contador_de_impares}")
numeral()