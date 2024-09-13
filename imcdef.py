import os
os.system("cls || clear")

def imc (n1, n2):
    imc_total = imc_peso / pow(imc_altura, 2)
    return imc_total


def resultadodeimc (imc_total):
   if imc_total < 18:
        print("você está abaixo do peso\nconsulte um  nutricionista para orientação")
   elif imc_total > 18.5 and imc_total < 24.9:
       print("você está com peso normal\nMantenha hábitos saudaveis!")
   elif imc_total > 25 and imc_total < 29.9:
       print("você está com sobrepeso\nConsidere uma dieta saudavel e atividade fisica!")
   elif imc_total > 30 and imc_total < 34.9:
       print("você está com obesidade grau 1\nprocure orientação de um profissional de saúde!")
   elif imc_total > 35 and imc_total < 39.9:
       print("você está com obesidade grau 2\nconsulte um medico para orientação")
   elif imc_total > 40  :
       print("você está com obesidade grau 3\nbusque assistência medica imiediatamente ")
 
       
imc_peso = float(input("Digite seu peso: "))
imc_altura = float(input("Digite sua altura: "))
imc_total = imc(imc_peso, imc_altura)
print(f"seu imc é de {imc_total}")
imc_total = resultadodeimc(imc_total)
