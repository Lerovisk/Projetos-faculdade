decimais = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0]
strings = ["a", "e", "i", "o", "u"]
booleans = [True, False, True, False, True]
vazio = [ ]

# O comando len() vai nos mostrar os iteráveis dentro de cada variável, por exemplo:
print(len(decimais))
print(len(strings))
print(len(booleans))
print(len(vazio))

# Como ficaria o print dessas listas:
print(decimais)
print(strings)
print(booleans)
print(vazio)
# Repare que o "[]" aparece junto.

# Uma curiosidade interessante: Podemos utilizar o len() como um contador também, exemplo:
inteiros = [5, 10, 15, 20]
print("\n APRESENTANDO LISTAS MÉTODO 1")
for i in range(len(inteiros)):
    print(inteiros[i])
    # inteiros[0] -> queremos acessar o índice/termo zero da lista INTEIROS (valor: 5)
    # inteiros[1] -> queremos acessar o índice/termo um da lista INTEIROS (valor: 10)
    # inteiros[2] -> queremos acessar o índice/termo dois da lista INTEIROS (valor: 15)
    # inteiros[3] -> queremos acessar o índice/termo três da lista INTEIROS (valor: 20)
    # inteiros[-1] -> queremos acessar o ÚLTIMO índice/termo da lista INTEIROS (valor: 20)
    # inteiros[-2] -> queremos acessar o PENÚLTIMO índice/termo da lista INTEIROS (valor: 15)
    # inteiros[-3] -> queremos acessar o ANTEPENÚLTIMO índice/termo da lista INTEIROS (valor: 10)...

#O [] já não aparece mais, e a lista passa a ser apresentada na vertical, isso por conta do [i].
# Sem o [i], a lista volta a aparecer na horizontal e com [].

print("\n APRESENTANDO LISTAS MÉTODO 2")
for i in inteiros:
    print(i)

print("\n APRESENTANDO LISTAS MÉTODO 3")
for i, elemento in enumerate(decimais):
    print(f" índice {i}: {elemento}")