import os
from dataclasses import dataclass 

os.system("cls || clear")



QTD = 2
#estrutura de dados
@dataclass
class Produto:
    nome_produto : str
    valor_do_produto : int

lista_produtos = []
for i in range(QTD):
    valor = Produto(
        nome_produto = input("Digite o nome do produto: "),
        valor_do_produto = int(input("Digite o valor do produto: "))
    ) 
    lista_produtos.append(valor)

soma = 0

for produto in lista_produtos:
    soma += produto.valor_do_produto
print(f"O valor total dos produtos foi de: {soma}")

# estrutura de dados
@dataclass
class Aluno:
    nome : str
    idade : int

lista_alunos = []
#solicitando dados 
print("\n===solicitando dados do aluno===")
for i in range(QTD):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_alunos.append(aluno)


#exibindo dados 
print("\n=== solicitando dados do usuario ===")
for aluno in lista_alunos:
   print(f"nome: {aluno.nome}")
   print(f"idade: {aluno.idade}")

nome_do_arquivo = "LIsta_de_alunos_SENAI.txt"
#abrindo arquivo e definindo que se rá feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_alunos:
   for aluno in lista_alunos:
       lista_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

print("\n=== Dados dos alounos salvo com sucesso!===")
#fechar conexão do arquivo
arquivo_alunos.close()

#lendo dados de uma arquivo.
#limpando a lista de alunos
print("\n===Acessando os dados de um arquivo")
with open(nome_do_arquivo,"r") as arquivo_de_origem:
   for linha in arquivo_de_origem:
       nome, idade = linha.strip().split(",")
       lista_alunos.append(Aluno(nome=nome, idade=int(idade)))
arquivo_alunos.close()


print("\n=== exibindo dados dos alunos do arquivo ===")
for aluno in lista_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")








#CRUD
#[x]CREATE
#[x]READ
#UPDATE
#DELETE