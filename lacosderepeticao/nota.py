import os
os.system("cls || clear")

nota = float (input("Digite sua nota: "))
while nota < 0 or nota > 10:
    print("\n A nota deve ser maior ou igual a 0 e menor e igual a 10. ")   
    nota = float (input("Digite sua nota novamente: "))
print(f"Sua nota foi {nota}")