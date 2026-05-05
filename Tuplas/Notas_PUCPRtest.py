#solicita as notas do usuario

nota1 = float(input("Qual a sua nota em matematica? "))
nota2 = float(input("Qual a sua nota em portugues? "))
nota3 = float(input("Qual a sua nota em ingles? "))
nota4 = float(input("Qual a sua nota em historia? "))
nota5 = float(input("Qual a sua nota em filosofia? "))

#calcula a media total das notas

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5.0

#verifica se a media eh maior que 7.0

if media >= 7:
    print(f"Voce obteve uma media de {media:.2f}, APROVADO!")
else:
    print(f"Voce obteve uma media de {media:.2f}, REPROVADO!")


