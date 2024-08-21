import os
os.system("cls || clear")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o seugundo numero: "))
print("o maior numero é: ")
if num1 < num2:
    print(num2 )
else:
    print(num1)

print("O menor número é: ")
if num1 > num2:
    print(num2)
else:
    print(num1)
