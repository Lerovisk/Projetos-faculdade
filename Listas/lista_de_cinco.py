'''Exercício de fixação 2: Crie um programa que solicite ao usuário duas listas com cinco elementos cada e,
como resultado, crie uma terceira lista que intercale os elementos das anteriores.'''

lista_1 = []
lista_2 = []
intercalados = []

print("Digite 5 numeros em cada lista.\n")
print("PRIMEIRA LISTA:")
for _ in range(5):
    num1 = int(input("Digite um numero: "))
    lista_1.append(num1)
print("SEGUNDA LISTA:")
for _ in range(5):
    num2 = int(input("Digite um numero: "))
    lista_2.append(num2)
for i in range(5):
    intercalados.append(lista_1[i])
    intercalados.append(lista_2[i])

print(f"Primeira lista: {lista_1}")
print(f"Segunda lista: {lista_2}")
print(f"Intercalados: {intercalados}")

