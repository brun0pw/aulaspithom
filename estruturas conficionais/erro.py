import os
os.system("clls || clear")

numero1 = float(input("Digite seu 1° número: "))
numero2 = float(input("Digite seu 2° número: "))

soma = numero1 + numero2
media = (numero1 + numero2) / 2
produto = numero1 * numero2

print(f" A soma de numero1 e numero2 foi: {soma}")
print(f" A média de numero1 e numero2 foi: {media}")
print(f" O produto de numero1 e numero2 foi: {produto}")

if numero1 < numero2:
  print("O menor número é: {numero1}")
else:
  print("O menor número é: {numero2}")