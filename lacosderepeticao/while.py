contador = 0
continua = 's'
while continua == 's':
 print("repetindo")
 contador +=1
 continua = input("tecle 's' se deseja continuar ").strip().lower()
  # quase um caracter o strip serve para tirar o espace

if contador == 0:
 print("o bloco NAO  foi repetido")
else:
 print(f"O bloco já foi repetido {contador} vezes")