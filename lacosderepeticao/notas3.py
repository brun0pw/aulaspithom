import os
os.system("clls || clear")
"""
escreva um algoritmo que esceva 3 notas de aluno
caso seja menor que 0 e maior que 10 mostre a pergunta novamente
calcule a média e caso a me dia for a partir de 7 ele está aprovado
caso seja entre 5 e 6.9 ele esta de recuperação
caso seja menor que 5 ele está reprovado
"""
quantidadedenotas = 3
soma = 0
for i in range(3):
 notas =  float(input(f"Digite sua {i + 1}° nota: "))
 soma += notas
 media = soma / quantidadedenotas

while True :
   
   if media >= 7:
      print("Aprovado")
      break
   elif media >= 5 or media >= 6.9:   
          print("você está de recuperação\n")
          break
   else:
       print("Você está perdido") 
       break
print(media)