"""Crie um programa que pergunte o tamanho de três lados de um triângulo e informe o tipo de triângulo, a saber:"""
print("Digite os tres lados do triangulo para identifica-lo.")
lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:     #vai testar se eh um triangulo

    if lado1 == lado2 and lado2 == lado3:   #vai testar se todos os lados sao iguais
        print("Triangulo Equilatero")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:   #vai testar se dois lados sao iguais
        print("Triangulo Isoceles")

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:    #vai testar se todos os lados sao diferentes
        print("Triangulo Escaleno")   #aqui tambem poderia ser somente else: print("Triangulo Escaleno")
else:
    print("Nao eh um triangulo")
