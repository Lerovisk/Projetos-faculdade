# Metodo 1 - Mais simples: Desse jeito podemos ter o mesmo resultado de um número porém
# de formas diferentes, segue explicação

num = 6 / 7

print('Resultado: %f' % num)  # mostra o resultado com 6 casas decimais

print('Resultado: %.2f' % num)  # mostra o resultado com 2 casas decimais

print('Resultado: %8.2f' % num)  # mostra o resultado com 8 espaços de digitação e 2 casas decimais

print('Resultado: %d' % num)  # mostra o resultado como inteiro

print('Resultado: %s' % num)  # mostra o resultado no seu modo string

# Metodo 2 - Esse é o metodo mais dificil, portanto nem pense em formatar desse jeito.
num = 6 / 7
outro_num = 10
t1 = "Hello"
t2 = "World"

print(f'Resultado: {num:f}')

print(f'Resultado: {num:.2f}')

print(f'Resultado: {num:8.2f}')

print(f'Resultado: {outro_num:8d}')

print(f'{t1:10}{t2:10}')

print(f'{t1:^10}{t2:^10}')

print(f'{t1:>10}{t2:>10}')

# Metodo 3 - Ok, esse tambem eh dificil

num = 6 / 7

outro_num = 10

t1 = "Hello"

t2 = "World"

print('Resultado: {0:f}'.format(num))

print('Resultado: {0:.2f}'.format(num))

print('Resultado: {0:8.2f}'.format(num))

print('Resultado: {0:8d}'.format(outro_num))

print('{0:10}{1:10}'.format(t1, t2))

print('{0:^10}{1:^10}'.format(t1, t2))

print('{0:>10}{1:>10}'.format(t1, t2))

# O importante eh que todos funcionam do mesmo jeito.
