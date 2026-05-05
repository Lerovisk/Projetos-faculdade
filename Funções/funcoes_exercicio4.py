'''Exercício de fixação 4: Documente a função fatorial() desenvolvida no exercício de fixação 1 desta unidade.'''


def fatorial(numero):
    '''
    Calcula o fatorial de um número inteiro.
    :param numero: número-base para o cálculo do fatorial
    :return: retorna o resultado do fatorial de um numero inteiro
    '''
    # segundo as propriedades de fatorial
    if numero == 0:
        return 1

    fat = 1
    for i in range(numero, 0, -1):
        fat *= i
    return fat
