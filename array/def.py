import os
os.system("cls || clear")
#função com retorno
def somar(n1, n2):
    soma = n1 + n2
    return soma

primeironumero = int(input("digite seu primeiro número: "))
sengundonumero = int(input("digite seu segundo número: "))

soma= somar(primeironumero, sengundonumero)
print(f"soma {soma}")