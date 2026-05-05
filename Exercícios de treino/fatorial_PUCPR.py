"""Elabore um programa que calcule o fatorial de um número, exibindo a informação de como é feito o cálculo.
 Exemplo: “O valor do fatorial de 5 é igual a 120. Expressão: 5*4*3*2*1”. """

fatorial = 1
por_extenso = " "
num = int(input(f"Digite um número para o cálculo do fatorial: "))

for i in range(num, 0, -1):                 #Vai comecar a conta ao contrario, ex[5,4,3,2,1]
    fatorial =  fatorial * i                #Vai acumular as multiplicacoes
    por_extenso = por_extenso + str(i)      #Vai guardar o valores em forma de strin, ex [5 4 3 2 1]
    if i > 1:                               #Vai verificar se o valor eh maior que 1 e se for:
        por_extenso = por_extenso + " * "  #Vai adicionar * em string ao seu lado, ex [5 * 4 * 3 * 2 * 1]

print(f"O valor do fatorial de {num}! é:{por_extenso} = {fatorial}")
