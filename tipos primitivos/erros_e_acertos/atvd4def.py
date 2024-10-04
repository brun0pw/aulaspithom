import os 
os.system("cls || clear")

def calularidade(n1, n2):
   
   idade = n2 - n1
   return idade

#entrada
idadeano = int(input("digite seu ano de nascimento: "))
anoquevoceesta = int(input("Digite em que ano você está? "))

#processamento
idade = calularidade(idadeano, anoquevoceesta )

#saída
print(f"sua idade é: {idade}")