import  os
os.system("cls || clear")

QUANTIDADEDENUMEROS = 5
numeros = []

def numeral():
 contador_de_pares = 0
 contador_de_impares = 0
 contador_de_positivos = 0
 contador_de_negativos = 0
 contador_numeros = 0
 while True:
     
      numero = int(input(f"Digite o  número: "))
      if numero == 0:
       print("==FIM==")
       break
      else:
        contador_numeros += 1
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
 print(f"A quantidade de numeros foi de {contador_numeros}\nO números positivos foram {contador_de_positivos}")
 print(f"Os números negativos foram {contador_de_negativos}\nOs números pares foram {contador_de_pares}  ")
 print(f"Os números ímpares foram {contador_de_impares}")
numeral()