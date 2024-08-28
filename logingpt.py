import os
os.system("cls || clear")
# Função para criar um novo usuário e senha
def criar_usuario_senha():
    usuario = input("Digite o nome de usuário para criar: ")
    senha = input("Digite a senha para criar: ")
    return usuario, senha

# Função principal
def main():
    # Criação do usuário e senha
    usuario_cadastrado, senha_cadastrada = criar_usuario_senha()
    
    while True:
        # Solicitação de login e senha
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        
        # Verificação se o login está correto
        condicao_corretamente = usuario == usuario_cadastrado and senha == senha_cadastrada
        
        # Saída do loop se as credenciais estiverem corretas
        while not condicao_corretamente:
            print("Login e senha incorretos")
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            condicao_corretamente = usuario == usuario_cadastrado and senha == senha_cadastrada
        
        print("Login bem-sucedido!")
        break  # Sai do loop principal após login bem-sucedido

if __name__ == "__main__":
    main()
