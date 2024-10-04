import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Habitante:
    nome: str
    idade: int
    sexo: str
    salario: int
@dataclass
class Dados_coletados:
     media_salarial: int
     maior_idade: int
     menor_idade: int
     quantidade_mulheres : int    
def media(a):
    media_salario = sum(a) / len(a)
    return media_salario
def menor_maior(a):
    menor = min(a)
    maior = max(a)
    return maior, menor


    
def organizar_tudo_numa_lista(lista_salario, lista_idade, quantidade_de_mulheres,dados_completos):
    media_salario = media(lista_salario)
    maior, menor = menor_maior(lista_idade)
    
    dados_coletados = Dados_coletados(
        media_salarial = media_salario,
        maior_idade = maior,
        menor_idade = menor,
        quantidade_mulheres = quantidade_de_mulheres
    ) 
    dados_completos.append(dados_coletados)
    return dados_completos
    
dados_completos = []    
lista_habitantes = []
lista_de_dados = []
lista_salario = []
lista_idade = []
quantidade_de_mulheres = 0
nome_do_arquivo = "Pesquisa_habitantes.txt"
while True:
    
    print("""
============================================
                PESQUISA IBGE      
============================================                
CÓDIGO      |    DESCRIÇÃO
 1          | ADICIONAR PESSOA
 2          | EXIBIR RESULTADOS E SAIR
============================================
    
    """)
    escolha = int(input("Digite a opção: "))
    if escolha == 1:
        habitante = Habitante(
             nome= input("Digite seu nome: "),
             idade= int(input("Digite sua idade: ")),
             sexo= input("Digite seu gênero: (M/F) ").upper(),
             salario= int(input("Digite seu salário: "))
                        )
        if habitante.sexo == "F" and habitante.salario >= 5000 :
            quantidade_de_mulheres += 1
        else:
            quantidade_de_mulheres = 0
        lista_habitantes.append(habitante)
        lista_salario.append(habitante.salario)
        lista_idade.append(habitante.idade)
        organizar_tudo_numa_lista(lista_salario, lista_idade,quantidade_de_mulheres,dados_completos)
       
        with open(nome_do_arquivo, "a") as todos_os_dados_pedidos:
            for lista in dados_completos:
                todos_os_dados_pedidos.write(f"{lista.media_salarial}, {lista.maior_idade}, {lista.menor_idade}, {lista.quantidade_mulheres}\n")
        print("Dados organizados e salvos com sucesso!")
        
    
    elif escolha == 2:
     if lista_habitantes == []:
       print("Nenhum habitante foi adicionando ainda!")
     lendo_arquivo = []
     with open(nome_do_arquivo, "r") as arquivo_de_origem:
       for linha in arquivo_de_origem:
        media_salarial, maior_idade, menor_idade, quantidade_mulheres = linha.strip().split(",")
        lendo_arquivo.append(Dados_coletados(media_salarial= float(media_salarial), maior_idade=int(maior_idade), menor_idade=int(menor_idade), quantidade_mulheres=int(quantidade_mulheres)))
        print("\n\n=== Exibindo dados dos alunos do arquivo ===")
        for aluno in lendo_arquivo:
            print(f"media salarial {aluno.media_salarial}")
            print(f"qtd mulheres: {aluno.quantidade_mulheres}")
            print(f"menor Idade: {aluno.menor_idade}")
            print(f"maior Idade: {aluno.maior_idade}")
     break
    else:
         print("===ERRO===")    
    
