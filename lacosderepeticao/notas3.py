import os
os.system("clls || clear")
"""
escreva um alos.system("clls || clear")goritmo que esceva 3 notas de aluno
caso seja menor que 0 e maior que 10 mostre a pergunta novamente
calcule a média e caso a me dia for a partir de 7 ele está aprovado
caso seja entre 5 e 6.9 ele esta de recuperação
caso seja menor que 5 ele está reprovado
"""
#definindo variaveis
quantidadedenotas = (1)
soma = 0
for i in range(quantidadedenotas):
   while True:
      notas =  float(input(f"Digite sua {i + 1}° nota: "))

      
# caso a nota seja errada a notas iram retornar com o mesmo valor que é 0
      if notas < 0 or notas > 10:
         print("===ERRO===")
         
      else : #somando a média
            soma += notas
            break
#calculando a media
media = soma / quantidadedenotas

#isso limpa o terminal
os.system("clls || clear")

# isso diz se a pessoa está aprovado ou não 
if media >= 7:
   print("Aprovado")
elif media >= 5:   
   print("você está de recuperação\n")
else : 
   print("Você está perdido!!") 



   