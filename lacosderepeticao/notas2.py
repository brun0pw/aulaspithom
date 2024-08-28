import os
os.system("cls || clear")

nota = float (input("Digite sua nota: "))
nota2 = float (input("Digite sua segunda nota: "))

while nota < 0 or nota > 10 and nota2 < 0 or nota2 > 10 :
    print("\n A nota deve ser maior ou igual a 0 e menor e igual a 10. ")   
    nota = float (input("Digite sua nota novamente: "))
    nota2 = float (input("Digite sua segunda nota novamente: "))
media = (nota + nota2) / 2
print(f"Sua nota foi {media}")