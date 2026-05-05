# AUTOMAÇÃO DE ÁREA
def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

# AUTOMAÇÃO DE PERÍMETRO
def calcular_perimetro_retangulo(largura, altura):
    perimetro = 2 * (largura + altura)
    return perimetro

# AUTOMAÇÃO DE APRESENTAÇÃO DE DADOS
def mostrar_dados(area, id_retangulo, perimetro):
    print(f"\n--- Analise de Retangulo {id_retangulo} ---")
    print(f"A area do retangulo {id_retangulo} eh: {area}")
    print(f"O perimetro do retangulo {id_retangulo} eh: {perimetro}")

# DADOS RETÂNGULO 1
largura1 = 10
altura1 = 5

# DADOS RETÂNGULO 2
largura2 = 5
altura2 = 5

# DADOS RETÂNGULO 3
largura3 = 5
altura3 = 20

# AREA E PERIMETRO DO RETÂNGULO 1
area1 = calcular_area_retangulo(largura1, altura1)
perimetro1 = calcular_perimetro_retangulo(largura1, altura1)

# AREA E PERIMETRO DO RETÂNGULO 2
area2 = calcular_area_retangulo(largura2, altura2)
perimetro2 = calcular_perimetro_retangulo(largura2, altura2)

# AREA E PERIMETRO DO RETÂNGULO 3
area3 = calcular_area_retangulo(largura3, altura3)
perimetro3 = calcular_perimetro_retangulo(largura3, altura3)

# APRESENTAÇÃO DE DADOS RETÂNGULO 1
mostrar_dados(area1, 1, perimetro1)

# APRESENTAÇÃO DE DADOS RETÂNGULO 2
mostrar_dados(area2, 2, perimetro2)

# APRESENTAÇÃO DE DADOS RETÂNGULO 3
mostrar_dados(area3, 3, perimetro3)

'''def processar_dados():
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))
    id = int(input("Digite o id do retangulo: "))
    area = calcular_area_retangulo(largura, altura)
    perimetro = calcular_perimetro_retangulo(largura, altura)
    mostrar_dados(area, id, perimetro)
    
    Funcao que poderiamos utilizar para otimizar ainda mais o nosso codigo'''


'''O codigo totalmente otimizado ficaria assim:
# PROCESSA OS DADOS INFORMADOS PELO USUÁRIO
def processar_dados():
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))
    id = int(input("Digite o id do retangulo: "))
    area = calcular_area_retangulo(largura, altura)
    perimetro = calcular_perimetro_retangulo(largura, altura)
    mostrar_dados(area, id, perimetro)
    
# AUTOMAÇÃO DE ÁREA
def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

# AUTOMAÇÃO DE PERÍMETRO
def calcular_perimetro_retangulo(largura, altura):
    perimetro = 2 * (largura + altura)
    return perimetro

# AUTOMAÇÃO DE APRESENTAÇÃO DE DADOS
def mostrar_dados(area, id_retangulo, perimetro):
    print(f"\n--- Analise de Retangulo {id_retangulo} ---")
    print(f"A area do retangulo {id_retangulo} eh: {area}")
    print(f"O perimetro do retangulo {id_retangulo} eh: {perimetro}")


processar_dados
processar_dados
processar_dados
'''
