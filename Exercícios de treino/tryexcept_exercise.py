""" Elabore um programa que solicite um número inteiro ao usuário,
 validando e imprimindo esse número."""

while True:     #Enquanto valor verdade, faca
    try:        #Tente isso
        num = int(input("Digite um numero inteiro: "))  #Pede ao usuario que digite um numero INTEIRO especificamente
        break       #Se o numero estiver correto o programa para de rodar
    except ValueError:         #Se o usuario digitar outra coisa alem de um numero inteiro, faca
        print("Valor invalido")

print("Número validado:", num)  #Imprime o valor validado




"""Elabore um programa que solicite um número decimal ao usuário,
 validando e imprimindo esse número."""

while True:
    try:
        num = float(input("Digite um numero decimal: ")) #Pede ao usuario que digite um numero DECIMAL especificamente
        break
    except ValueError:
        print("Valor invalido")

print("Numero validado: ", num)




"""Elabore um programa que solicite um número inteiro ao usuário, que esteja dentro do intervalo 1 a 5
 validando e imprimindo esse número."""

while True:
    try:
        num = int(input("Digite um numero inteiro entre 1 e 5: "))
        if 5 >= num >= 1:
            break
        else:
            print("O numero deve estar entre 1 e 5.")
    except ValueError:
        print("Valor invalido")
print("Numero validado: ", num)
