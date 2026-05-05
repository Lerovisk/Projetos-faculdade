'''
soma = 0
cont = 0
media = 0
while True:
    num = int(input("Digite um numero (0 para encerrar): "))
    if num == 0:
        break
    else:
        cont += 1
        soma += num
if cont == 0:
    print("Nenhum numero foi inserido")
else:
    media = soma / cont
    print(f"A media dos numeros eh: {media}'''


oi = [1,2,3]
soma = sum(oi)
media = soma / len(oi)
print(media)


