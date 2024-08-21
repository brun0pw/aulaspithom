

# Pedindo ao usuário se ele deseja criar um novo usuário
resposta = int(input("Deseja fazer um novo usuário?\nDigite 1 para sim, \nDigite 2 para não: "))
if resposta == 1:
    novousuario = input("Qual é o novo nome do usuário? ")
    novasenha = input("Qual é sua nova senha? ")
else :
    print("erro")



# Solicitando o login do usuário
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

# Verificando se as credenciais estão corretas
if usuario == novousuario and senha == novasenha:
    print("Bem-vindo, Sr. " + usuario)
else:
    print("Login ou senha inválidos, tente novamente.")