"""informe por meio de uma funçao a media
informe por meio de uma funcao se a media for maior ou igual a a 7 o aluno esta aprovado
"""
import os 
os.system("cls || clear")
QUANTIDADEDENOTAS = 3

def notafim(nota):
 nota += nota
 media = nota / QUANTIDADEDENOTAS
 return media
os.system("cls || clear")


def mediafim(media):
 
 if media >= 7:
  return "Prabéns!! você foi aprovado!"

 else :
  return "você foi reprovado!"
 



 
for i in range(QUANTIDADEDENOTAS):
  nota = int(input(f"Digite sua {i + 1} nota: "))
media = notafim(nota) 
media = mediafim(media)
print(media)

  
