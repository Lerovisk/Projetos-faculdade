"""Crie um programa que gere a série de Fibonacci enquanto o valor for
menor que um valor informado pelo usuário. Observação:
série de Fibonacci = 0, 1, 1, 2, 3, 5, 8... é formada por 0, 1 e,
partir deste ponto, sempre será a soma dos dois valores anteriores."""


valor_limite = int(input("Informe o valor-limite: "))   #Pede para o usuario estabelecer um limite
valor = 0
num1 = 0
num2 = 1           #Vai sempre começar em 0 + 1
serie = "0, 1"     #Vai fazer a parte extensa do calculo para ser apresentada

while valor < valor_limite:
    valor = num1 + num2
    if valor < valor_limite:
        num1 = num2
        num2 = valor
        serie += ", " + str(valor)
print(f"Fibonacci: {serie}")