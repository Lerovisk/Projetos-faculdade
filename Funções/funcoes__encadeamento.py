'''Exemplo de aplicação 5: Elabore um programa que, aplicando a fórmula de Bhaskara por funções,
encontre as raízes de um polinômio do segundo grau'''


def delta(a, b, c):                 # Criamos uma função para calcular somente o delta
    """
     Calcula o valor de delta utilizado no cálculo de raízes de polinômios de segundo grau.

    :param a: Valor do primeiro termo do polinômio.
    :param b: Valor do segundo termo do polinômio.
    :param c: Valor do termo independente do polinômio.
    :return : Retorna as raízes calculadas e um booleano, indicando se o cálculo foi bem-sucedido.
    """
    return b * b - 4 * a * c        # Não criamos uma variável ainda

def bhaskara(a, b, c):
    d = delta(a, b, c)      # Agora sim, delta é uma variável
    if d < 0:           # Se delta for menor que zero
        print("As raízes são imaginárias")
        return 0, 0, False  # Retorne dois zero(raízes) e declare como falso
    else:       # Se não, faça o cálculo restante
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2, True    # Retorne os valores das raízes e declare como verdadeiro

# Valores amostrais 1
print("-------- Bhaskara dos valores: a = 1, b = 3, c = 1 --------")
result1 = bhaskara(1, 3, 1)
if result1[2]:
    print(f"As raízes são {result1[0]:.2f} e {result1[1]:.2f}")


# Valores amostrais 2
print("\n-------- Bhaskara dos valores: a = 1, b = 2, c = 1 --------")
result2 = bhaskara(1, 2, 1)
if result2[2]:
    print(f"As raízes são {result2[0]:.2f} e {result2[1]:.2f}")

# Valores amostrais 3
print("\n-------- Bhaskara dos valores: a = 1, b = 1, c = 1 --------")
result3 = bhaskara(1, 1, 1)
if result3[2]:
    print(f"As raízes são {result3[0]:.2f} e {result3[1]:.2f}")