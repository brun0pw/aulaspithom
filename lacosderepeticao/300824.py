import os
os.system("clls || clear")
"""
escreva um alos.system("clls || clear")goritmo que esceva 3 notas de aluno
caso seja menor que 0 e maior que 10 mostre a pergunta novamente
calcule a média e caso a me dia for a partir de 7 ele está aprovado
caso seja entre 5 e 6.9 ele esta de recuperação
caso seja menor que 5 ele está reprovado
"""
#definindo variaveis
quantidadedenotas = 1
soma = 0
respostanum = 1
contador = 0

os.system("clls || clear")
while True:
        notas =  float(input(f"Digite uma nota: "))
       
        resposta = input("""   deseja colocar mais uma nota ? 
                        responda em s para sim e n para não      """).upper()
       
        if resposta == "S":
           quantidadedenotas += 1 
           contador += 1
           soma += notas
           
    # caso a nota seja errada a notas iram retornar com o mesmo valor que é 0
                
        else : #somando a média
            soma += notas
            break
#calculando a media
#calculando a media
media = soma / quantidadedenotas 





# isso diz se a pessoa está aprovado ou não 
if media >= 7:
   print("Aprovado")
elif media >= 5:   
   print("você está de recuperação\n")
else : 
   print("Você está perdido!!") 
print(f" sua media foi: {media}")
print(f"você colocou {quantidadedenotas} notas")

   