""" Elabore um programa que solicite ao usuário dez números e efetue a multiplicação,
exibindo o resultado. No entanto, se em algum momento o número digitado for 0,
deve pular esta iteração, para que o valor não seja zerado."""

mult = 1
for i in range (10):
    num = int(input("Digite o " + str(i + 1) + "o número: "))
    if num == 0:                   #Se o numero for igual a 0, continue/ignore.
        continue
    mult *= num
print("A multiplicação dos números é", mult)