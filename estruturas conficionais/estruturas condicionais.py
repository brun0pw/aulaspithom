import os
os.system("cls || clear")


# solicitando dados
idade =  int(input("Digite sua idade: "))

#verificando 
#true is verdadiro and false is falso
if idade < 18:
    print("é menor de idade e criança")
elif  idade >= 18 and idade < 21:
    print("é maior de idade e jovem")
if idade >= 21:
    print("é maior de idade e adulto")
