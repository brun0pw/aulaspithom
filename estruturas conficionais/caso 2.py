import os
os.system("cls || clear")
  

print("          bem vindo ao restaurante       ")
print("""
                === menu ===
        |código |     prato       |   valor  |
        |   1   |    picanha      |   25,00  |
        |   2   |    lasanha      |   20,00  |
        |   3   |   strogonoff    |   18,00  |
        |   4   |  bife acebolado |   15,00  |
        |   5   |   pão com ovo   |    5,00  |
      
""")

opcao = int (input("Escolha a opção: "))
match(opcao):
  case 1:
    print("o prato escolhido foi: picanha  \nValor a ser pago : 25,00")

  case 2:
    print("o prato escolhido foi: lasanha  \nValor a ser pago : 20,00")

  case 3:
    print("o prato escolhido foi: strogonoff  \nValor a ser pago : 18,00")

  case 4:
    print("o prato escolhido foi: bife acebolado \nValor a ser pago : 15,00")

  case 5:
    print("o prato escolhido foi:  pão com ovo  \nValor a ser pago : 5,00")
  
  case _:
    print("ERRO")
print("==FIM==")