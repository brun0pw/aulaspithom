import os 
os.system("cls || clear")



#entrada
QUANTIDADEDENOTAS = 4
lista_notas = []
media = []
mediafinal = 0
somanotas = 0
#os for 
for i in range(QUANTIDADEDENOTAS):
    notas = float(input("digite sua nota: "))
    lista_notas.append(notas)
    somanotas += notas
    mediafinal = somanotas / QUANTIDADEDENOTAS
media.append(mediafinal)

#saída de dados
for i,  notas in enumerate(lista_notas):
 print(f"sua {i + 1}ª nota é: {notas} ")
 os.system("cls || clear")

print(f" suas medias foram: {lista_notas}")
#média se a pessoa está passada na média ou não
if mediafinal >= 7:
   print(f"você passou com média {mediafinal}")
elif mediafinal >= 5:
   print(f"você está com recuperação com média {mediafinal}")
else:
   print(f"você perdeu com média {mediafinal}")