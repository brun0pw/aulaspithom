import os
os.system("cls || clear")



print("Digite suas notas e descubra suas média")
soma = 0
media = 0
for i in range(1,4):
  numero = int(input(f"Digite a {i}° nota: "))
  soma = soma + numero 
  
  
media  = (media + soma) / i
print(f"Sua média foi = {media}")
if(media >= 7):
  print("você está aprovado!!")
else:
  if (media >= 4):
   print("você está reprovado")
  else:
   print("você está perdido")