'''Exercício de fixação 1: Crie um programa que calcule, a partir de uma função,
o fatorial de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.'''

def fatorial(numero):
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1

    fat = 1         # Criando a variavel dentro da funcao
    for i in range(numero, 0, -1):      # range(Inicio, limite, passo)
        fat *= i        # fat = fat * i     # o coputador sempre comeca pelo numero antescedente, ou seja, se 5, entao inicia no 4
    return fat

numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
fat = fatorial(numero)
print(f"O fatorial de {numero} é {fat}")