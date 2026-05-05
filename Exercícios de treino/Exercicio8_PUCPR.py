"""Crie um programa que simule um caixa eletrônico.
O programa deverá perguntar ao usuário o valor do saque e depois informar quantas
notas de cada valor serão fornecidas,a saber:
Notas disponíveis: 1, 5, 10, 50 e 100 reais.
Valor mínimo de saque: R$ 10,00.
Valor máximo de saque: R$ 600,00."""

valor = int(input("Qual valor deseja sacar? "))
resto = valor
sobra = 0
n1 = n5 = n10 = n50 = n100 = 0 #Inicia número de notas em zero


if valor < 10.0 or valor > 600.0:            #Precisamos da variavel valor para testar se esta dentro das exigencias
    print("Saque menor que o valor mínimo ou excede o valor máximo.")
else:
    if resto >= 100:            #Se o valor for maior ou igual a cem
        sobra = resto % 100       #Vai dividir o valor por cem e ver quanto sobra
        n100 = int((resto - sobra) / 100) #Se sobrar 0 o resto / 100 = n100
        resto = sobra  #Resto vai passar a valr de novo ou zerar, isso no caso de um numero como 250.
    if resto >= 50:         #O ciclo repete porem agora com as notas de 50
        sobra = resto % 50
        n50 = int((resto - sobra) / 50)
        resto = sobra
    if resto >= 10:
        sobra = resto % 10
        n10 = int((resto - sobra) / 10)
        resto = sobra
    if resto >= 5:
        sobra = resto % 5
        n5 = int((resto - sobra) / 5)
        resto = sobra
        n1 = resto

    print("Notas de 100:", n100)
    print("Notas de 50:", n50)
    print("Notas de 10:", n10)
    print("Notas de 5:", n5)
    print("Notas de 1:", n1)




