import os
os.system("cls || clear")
sexo = input("""Qual é seu sexo?
                   m para masuclino
                   f para feminino
              """).lower()
peso = float(input("Quanto você pesa? "))
altura = float(input("Qual é a sua altura? "))
pesoideal = 0
match(sexo):
    case "m":
        pesoideal = 72.7 * altura - 58
     

    case "f": 
        pesoideal = 62.1 * altura - 44.7
       
print(f"Seu peso ideal é de {pesoideal: .1f}")