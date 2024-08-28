import os
os.system("cls || clear")

novologin = input("Digite seu novo login: ")
novasenha = input("Digite sua nova senha: ")
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

while login != novologin and novasenha != senha:
      print("senha ou login incorretos")
      login = input("Digite seu login: ")
      senha = input("Digite sua senha: ")
      print("==FIM==")
      break