num = int(input("Digite o valor do numerador: "))
exp = int(input("Digite o valor do expoente: "))
result = 1    #Vai receber o valor de num
for i in range(exp):   #Vai multiplicar o numero por ele mesmo tantas vezes
    result *= num   #Aqui ele vai receber 1 * num, ou seja, num
print(num, "elevado a", exp, "é igual a", result)


'''Outro jeito muito mais simples de fazer seria fazer num**exp, assim:
num = int(input("Digite o valor do numerador: "))
exp = int(input("Digite o valor do expoente: "))
print(f"{num} elevado a {exp} eh {num*exp}")
'''