def calculo_imc(lista_de_pessoas):
    for pessoa in lista_de_pessoas:
        altura = pessoa['altura']
        peso = pessoa['peso']
        imc = peso / (altura ** 2)
        print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')

# Dados das pessoas em formato de lista de dicionários
pessoas = [
    {'nome': 'João', 'altura': 1.75, 'peso': 70},
    {'nome': 'Maria', 'altura': 1.60, 'peso': 55},
    {'nome': 'Carlos', 'altura': 1.80, 'peso': 90}
]

# Cálculo do IMC para cada pessoa
calculo_imc(pessoas)

print("\nContinuando o cálculo para uma nova lista de pessoas.")

# Dados das pessoas em formato de lista de dicionários
novas_pessoas = [
    {'nome': 'Cézar', 'altura': 1.78, 'peso': 79},
    {'nome': 'Marta', 'altura': 1.61, 'peso': 52},
    {'nome': 'Ana', 'altura': 1.65, 'peso': 70}
]

# Cálculo do IMC para cada pessoa
calculo_imc(novas_pessoas)

print("\nAgora, vamos para a lista final.")

# Dados das pessoas em formato de lista de dicionários
mais_pessoas = [
    {'nome': 'Julia', 'altura': 1.53, 'peso': 51}
]

# Cálculo do IMC para cada pessoa
calculo_imc(mais_pessoas)

'''O conceito de caixa-preta: não importa a linha que chamemos a função calcular_imc(),
ela fará o cálculo sem precisarmos saber como ela faz isso.'''
