import os
os.system("cls || clear")


#função sem retorno
def logo_senai():
   os.system("cls || clear")
   print(""" 
=========
  SENAI 
========= 
""")
logo_senai()
nome = input("digite seu nome: ")

logo_senai()
idade = int(input("digite sua idade: "))


logo_senai()
print(f"olá {nome}, sua idade é {idade} anos")