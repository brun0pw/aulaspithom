import os
os.system("cls || clear")
from dataclasses import dataclass

#ele quer a média do salari/ maior e menor idade do gp/ quantidade de mulheres com 5.000 acima

#criando uma classe para pessoa
@dataclass
class Pessoa :
    nome : str
    idade : int
    sexo : str
    salario : float

#criando uma lista para pessoa e salario e quantidade de mulheres
lista_pessoa = []
lista_idade = []
lista_salario = []
#criando um contador para a lista de mulheres
qtd_mulheres = 0
#criando o def para média salarial e para maior e menor idade
def menor_maior (lista_salario):
    menor = min(lista_salario)
    maior = max(lista_salario)
    return menor, maior
    
def media (a):
    media_ = sum(a) /  len(a)
    return media_
#criando um menu
print("===PESQUISA IBGE===")
#cria um arquivo
nome_do_arquivo = "pesquisa_habitantes.txt"

while True:
    print("""
====MENU====
Código | Descrição
    1  | Adicionar pessoa
    2  | Exibir resultados
    3  | Sair      """)
    escolha = int(input("Digite a opção: "))
    os.system("cls || clear")
    match escolha:
        case 1:
            #solicitando dados
            pessoa = Pessoa(
                nome = input("Digite seu nome: "),
                idade = int(input("Digite sua idade: ")),
                sexo = input("Digite seu sexo: (responda apenas com M/F) ").upper(),    
                salario = float(input("Digite quanto você ganha mensalmente: ")))
            #adicionando a pessoa, o salario e a idade da pessoa
            lista_pessoa.append(pessoa)
            lista_salario.append(pessoa.salario)
            lista_idade.append(pessoa.idade)
            os.system("cls || clear")
            #arquivando os dados do user
            with open  (nome_do_arquivo, "a") as todas_as_pessoas:
                        for pessoas in lista_pessoa :
                            todas_as_pessoas.write(f"{pessoas.nome}, {pessoas.idade}, {pessoas.sexo}, {pessoas.salario} \n")
            #pergutando ao user se ele quer continuar
            opcao = input("Deseja continuar ? (responda apenas com S/N)").upper()
            #adicionando o contador de mulheres
            if pessoa.sexo == "F" and pessoa.salario >= 5000:
               qtd_mulheres += 1
            #perguntando se o user vai querer continuar
            if opcao != "S":
                break
            #media salarial
            media_salarial = media(lista_salario)
            #maior e menor idade
            menor, maior = menor_maior(lista_idade)
            
                        
            
            
            os.system("cls || clear")
        case 2:
            lista_pessoa = []
            #exibindo dados
            print("\n=== Resultados ===")
            with open(nome_do_arquivo, "r") as arquivo_de_origem:
                for linha in arquivo_de_origem:
                    nome, idade, sexo, salario = linha.strip().split(",")
                    lista_pessoa.append(Pessoa(nome=nome, idade=(int(idade)), sexo= sexo, salario=float(salario)))

                    # Adicionando para cálculos
                    lista_idade.append(idade)
                    lista_salario.append(salario)
        case 3:
            break 

