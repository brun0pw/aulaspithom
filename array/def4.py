import os
os.system("cls || clear")
 #esse def soma 
def somar (n1,n2):
 soma =  n1 + n2
 print("O resultado foi: ")
 print(soma)
 return soma
 

 #esse subtrai
def subtrair (n1,n2):
 subtracao =  n1 - n2
 print("O resultado foi: ")
 print(subtracao)
 return subtracao

#esse multiplica
def multiplicacao (n1,n2):
 mult =  n1 * n2
 print("O resultado foi: ")
 print(mult)
 return mult

#esse divide
def divisao (n1,n2):
 dividir =  n1 / n2
 print("O resultado foi: ")
 print( dividir)
 return dividir


#aqui inicia a calculadora e pede os dois números
print("Bem vindo a calculadora!", sep =  '-')
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# isso pede ao user que operação ele vai querer
print ("""
+ para adição 
- para subtração
* para multiplicação
/ para divisão
""")
opcao = input("escolha a opção ")
os.system("cls || clear")
#e aqui eu crio um match para imprimir só a operação que o user escolheu
match (opcao):
    case "+":
       soma = somar(num1, num2)
    case "-":
        
        subtracao = subtrair(num1, num2)
    case "*":
    
   
        mult = multiplicacao(num1, num2)
    case "/":
         dividir = divisao(num1,num2)
    case _ :  
        print("Error 1")


print("==FIM==")



