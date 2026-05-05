"""Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas.
 Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:"""

print("Digite as quatro notas bimestrais da disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
faltas = int(input("Quantas faltas voce teve nesse bimestre? "))

media = (nota1 + nota2 + nota3 + nota4) / 4
presenca = ((40 - faltas) / 40) * 100

if media >= 7 and faltas >= 40 * 0.25:
    result = "Aprovado"
else:
    result= "Reprovado"

print(f"Sua media foi {media}")
print(f"Presenca: {presenca}%")
print(f"Você foi {result}!")