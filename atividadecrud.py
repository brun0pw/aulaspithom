import os
from dataclasses import dataclass


os.system("cls || clear")


# Estrutura de dados
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade : int
    peso : float
    altura : float

QUANTIDADE_ALUNOS = 4


#solicitando dados
alunos = []
for i in range(QUANTIDADE_ALUNOS):
    aluno = Cliente(
        nome = input("Digite seu nome: "),
        sobrenome = input("Digite seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite seu altura: "))
    )
    alunos.append(aluno) 


#exibindo dados
print("\n=== Exibindo dados ===")
for clthanos in alunos:
    print(f"Nome: {clthanos.nome} ")
    print(f"Sobrenome: {clthanos.sobrenome} ")
    print(f"Idade: {clthanos.idade} ")
    print(f"Seso: {clthanos.peso} ")
    print(f"Altura: {clthanos.altura} ")
    

#Salvar em um arquivo chamado: carteira_de_clientes.txt
nome_do_arquivo = "carteira_de_clientes.txt"


with open(nome_do_arquivo, "a") as todos_alunos:
    for clthanos in alunos:
        alunos.write({clthanos.nome}, {clthanos.sobrenome}, {clthanos.idade},{clthanos.peso},{clthanos.altura})

todos_alunos.close()
#Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal.

alunos = []
with open (nome_do_arquivo, "r") as todos_alunos:
    for linha in todos_alunos:
        nome,sobrenome,idade,peso, altura = linha.strip().split(",")
        alunos.append(Cliente(nome=nome,sobrenome=sobrenome, idade=int(idade),peso = float(peso), altura=float(altura)))


print("\n=== exibindo dados dos alunos do arquivo ===")
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"sobrenome: {aluno.sobrenome}")
    print(f"Idade: {aluno.idade}")
    print(f"Peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")