import os
os.system("cls || clear")

# solicitando dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
notas1 = float(input("Digite sua primeira nota: "))
notas2 = float(input("Digite sua segunda nota: "))
notas3 = float(input("Digite sua terceira nota: "))
media = (notas1+ notas2 + notas3) / 3

#imprimindo dados
print("\nImprimindo resultados: ")
print (f"Nome do aluno: {nome}")
print (f"Idade: {idade}")
print (f"Sua média foi: {media}")

#verificando dados
if media >= 7 : 
   print(f"parabéns!! você foi aprovado.")
if media >= 4 : 
   print(f"Você está de recuperação.")
   resposta = input("Você quer fazer a recuperação? ")
   if resposta == "sim":
      print("Você receberá o link pelo seu e-mail")
   else:
      print("Você está reprovado!")

else:
   print("Você está reprovado!")   