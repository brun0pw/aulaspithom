import os 
os.system("cls || clear")

def multiplicacao (n1,n2):
    mult = n1 * n2
    
    resultado = print(f" {numero} * {n2} é {mult}")
    return mult, resultado
    
numero = int(input("digite o número e veja a tabuada dele: "))
print (f"a tabuada do {numero} é:")
for i in range(1,11):
  mult = multiplicacao(numero, i)






