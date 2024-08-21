import os
os.system("cls || clear")

print("Bem-vindo ao sistema de votação")
idade = int(input("\nQuantos anos você têm? "))
if idade >= 18 and idade <=65 :
    print ("Você é obrigado a votar") 
else :
    print("Você não é obrigado a votar")