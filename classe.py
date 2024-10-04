from dataclasses import dataclass
import os

os.system("cls || clear")


#
@dataclass
class Aluno:
    nome : str
    idade : int
    media : float

#criando a lista de alunos
lista_alunos = []

for i in range(3):
    print(f"==Solicitando dados do {i+1}º aluno.==")

    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("Dgite a idade: ")),
        media = float(input("Digite sua média: ")) 
    )
    os.system("cls || clear")
    lista_alunos.append(aluno)


#processamento.
lista_media = []

for aluno in lista_alunos:
    lista_media.append(aluno.media)


media = sum(lista_media) / len(lista_alunos)
#saida de dados
print("==Exibindo dados==")


for aluno_ in lista_alunos:
    print(f"Nome: {aluno_.nome}")
    print(f"idade: {aluno_.idade}")
    print(f"média: {aluno_.media}")
    os.system("cls || clear")
print(f"Média: {media}")


