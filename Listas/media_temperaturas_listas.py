'''Exercício de fixação 3: Crie um programa que leia as temperaturas médias de cada mês do ano
e as armazene em uma lista; use outro vetor para guardar e exibir, quando necessário,
o nome dos meses do ano; calcule a média anual de temperatura e informe quais meses ficaram acima da média anual.'''

temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp_media = 0

print("Digite a temperatura media de cada mes.\n")

for mes in meses: # Percorre pelos nomes na lista meses, do inicio ao fim.
    medias_mensais = float(input(f"Temperatura média em {mes}: "))
    temperaturas.append(medias_mensais)     #   Adiciona a temperatura media do mes na lista de temperaturas.

media_anual = sum(temperaturas) / len(temperaturas)    #    Calcula a media anual, somando as medias mensais e dividindo por 12.

print(f"\nMeses com temperatura acima de {media_anual:.1f} graus: ")
for i in range(12):
    if temperaturas[i] >= media_anual:     # Se alguma temperatura for acima ou igual a media anual.
        print(f"{meses[i]}: {temperaturas[i]:.1f} graus")   #Diga o mes e sua temperatura.
