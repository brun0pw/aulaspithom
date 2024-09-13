"""
crie um algoritmo que aceite apenas 6 valores inteiros, positivos e pares, em seguida, mostre na tela os valores lidos na ordem inversa.
caso seja informado um número diferente dos criterios apresentados acima, repita a pergunta para o usuario


"""
import os
os.system("cls || clear")
QTD = 6
numero = []
def positivoeoperante():
 for i in range(QTD): 
  while True: 
   numeros = int(input(f"Digite o {i + 1}° numero: "))
   if numeros > 0 and numeros %2 == 0:
   
    numero.append(numeros)
    break
   else:
     print("===ERRO===\n digite um número par, positivo e inteiro.")

positivoeoperante()


#saida de dados
for i, numeros1 in enumerate(reversed(numero)):
 print(f" numero {numeros1}")