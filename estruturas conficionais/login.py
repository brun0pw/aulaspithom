
import os
os.system("cls || clear")
  

#pedindo o usuário o que ele quer
resposta = input(f"deseja fazer um novo usuario?\nse sim Digite 1, \nse não digite 2: ")


    #fazendo o novo usuario
if(resposta == "1"):
    novousuario =  input(f"qual é o novo nome do usuario? ") 
    novasenha = input(f"qual é sua nova senha? ")
    usuario = input(f"Digite seu nome do usuario: ")
    senha = input(f"digite sua senha: ")
else:  
    print("erro")
    
    
#pedindo ao user o novo login dele
if usuario == novousuario and senha == novasenha:
     print(f"bem vindo Sr: " + usuario)
else :
    print(f"login ou senha inválidos, tente novamente;") 
     




      
   
