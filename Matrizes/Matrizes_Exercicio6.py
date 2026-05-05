'''Solicite ao usuário que digite três coordenadas (x, y), armazenando-as em uma matriz bidimensional.'''

coordenadas = [] # Começamos criando uma lista vazia chamada coordenadas, que servirá para armazenar as coordenadas fornecidas pelo usuário.

for i in range(3): # Entramos em um laço "for" que será executado três vezes (de 0 a 2).
    x = int(input("Insira um valor de x: ")) #  Pedimos ao usuário para fornecer um valor para x
    y = int(input("Insira um valor de y: ")) # Pedimos ao usuário para fornecer um valor para y
    coordenadas.append([x, y]) # Adicionamos um par de coordenadas, que é uma lista contendo x e y, à lista coordenadas.

print(coordenadas) # Finalmente, depois que todas as três coordenadas foram coletadas e armazenadas, imprimimos a lista coordenadas.