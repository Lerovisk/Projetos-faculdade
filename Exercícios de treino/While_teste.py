"""CENÁRIO 2: WHILE COM FLAG
Aqui, a corrida continua enquanto a variável combustivel for maior que 0.
A cada volta, o combustível diminui. A condição não é um simples contador,
mas o estado de uma variável que muda, tornando o loop mais dinâmico."""

combustivel = 100
voltas = 0
while combustivel > 0:
    print(f"Volta {voltas + 1}, combustível: {combustivel}%")
    combustivel -= 15
    voltas += 1
print("Fim de corrida, sem combustível!")


"""Exemplo de aplicação 6: Elabore um programa que solicite ao usuário que digite indefinidamente números e efetue a 
soma, parando apenas quando o usuário digitar o número 0."""
soma = 0
num = -1    #Atribuimos o valor -1 pois a condicao eh que ele seja igual a zero
contador = 1
while num != 0:
    num = int(input(f"Digite o {contador}o numero (0 Finaliza a contagem): "))
    soma += num
    contador += 1

print(f"A soma dos numeros eh : {soma}")

"""OUTRO MODO DE FAZER SERIA ASSIM:
soma = 0
num = -1
while True:
    num = int(input("Digite um número para somar (0 finaliza): "))
    if num == 0:
        break;
    soma += num
print("A soma dos números é ", soma)"""