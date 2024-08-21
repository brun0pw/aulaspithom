import os
os.system("cls || clear")

opcao = int(input("""Digite um dia da semana:
                            1 para domingo 
                            2 para segunda
                            3 para terça
                            4 para quarta
                            5 para quinta
                            6 para sexta
                            7 para sábado
              """))
match(opcao):
    case 1|7:#final de semana
        print("Domingo, Final de semana")
    
    case 2|3|4|5|6 :#dia de semana
        print("Segunda-feira, dia de ressaca, mas continua sendo util")
   

    case _ :
        print("INVÁLIDO")
   
