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
class DadosColetados:
    media_salarial: float
    maior_idade: int
    menor_idade: int
    quantidade_mulheres: int

def media(a):
    soma = sum(a)
    divisao = len(a)
    media_salario = soma / divisao
    return media_salario

def menor_maior(a):
    menor = min(a)
    maior = max(a)
    return maior, menor

def organizar_tudo_numa_lista(lista_salario, lista_idade, quantidade_de_mulheres, dados_completos):
    media_salario = media(lista_salario)
    maior, menor = menor_maior(lista_idade)
    
    dados_coletados = DadosColetados(
        media_salarial=media_salario,
        maior_idade=maior,
        menor_idade=menor,
        quantidade_mulheres=quantidade_de_mulheres
    ) 
    dados_completos.append(dados_coletados)
    return dados_completos
    
dados_completos = []    
lista_habitantes = []
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
            nome=input("Digite seu nome: "),
            idade=int(input("Digite sua idade: ")),
            sexo=input("Digite seu gênero: (M/F) ").upper(),
            salario=int(input("Digite seu salário: "))
        )
        
        if habitante.sexo == "F" and habitante.salario >= 5000:
            quantidade_de_mulheres += 1
            
        lista_habitantes.append(habitante)
        lista_salario.append(habitante.salario)
        lista_idade.append(habitante.idade)
        organizar_tudo_numa_lista(lista_salario, lista_idade, quantidade_de_mulheres, dados_completos)
       
        with open(nome_do_arquivo, "a") as todos_os_dados_pedidos:
            for lista in dados_completos:
                # Corrigido para usar vírgula corretamente
                todos_os_dados_pedidos.write(f"{lista.media_salarial}, {lista.maior_idade}, {lista.menor_idade}, {lista.quantidade_mulheres}\n")
        print("Dados organizados e salvos com sucesso!")
        
    elif escolha == 2:
        if not lista_habitantes:
            print("Nenhum habitante foi adicionado ainda!")
        else:
            lendo_arquivo = []
            with open(nome_do_arquivo, "r") as arquivo_de_origem:
                for linha in arquivo_de_origem:
                    media_salarial, maior_idade, menor_idade, quantidade_mulheres = linha.strip().split(", ")
                    lendo_arquivo.append(DadosColetados(
                        media_salarial=float(media_salarial),
                        maior_idade=int(maior_idade),
                        menor_idade=int(menor_idade),
                        quantidade_mulheres=int(quantidade_mulheres)
                    ))

            # Exibir os dados lidos do arquivo
            for dados in lendo_arquivo:
                print(f"\nMédia Salarial: R$ {dados.media_salarial:.2f}")
                print(f"Maior Idade: {dados.maior_idade}")
                print(f"Menor Idade: {dados.menor_idade}")
                print(f"Quantidade de Mulheres com salário >= R$ 5.000,00: {dados.quantidade_mulheres}")
        break
    
    else:
        print("=== ERRO === Opção inválida! Tente novamente.")
