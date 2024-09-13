import os
os.system("cls || clear")
#função com retorno
def media (n1, n2):
    dividir = (n1 + n2) / 2
    
    return dividir
primeironumero = int(input("digite o primeiro número: "))
segundonumero = int(input("digite o sengundo número: "))

dividir = media(primeironumero, segundonumero)

print(f"sua media foi de: {dividir}")