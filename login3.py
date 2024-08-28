import os
os.system("cls || clear")
numtentativas = 0


novologin = input("Digite seu novo login: ")
novasenha = input("Digite sua nova senha: ")
os.system("cls || clear")

while True :
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login != novologin or novasenha != senha:
      print("senha ou login incorretos")
      numtentativas += 1
      if numtentativas == 3:
          print("limite de tentativas alcançado\n", numtentativas)
          break
    else:
       print("bem vindo")