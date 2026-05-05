ano_atual = 2026
nascimento = int(input("Qual é o seu ano de nascimento? "))

resp = input("Você já fez aniversário neste ano? ")

idade = ano_atual - nascimento

if resp == "nao":
    idade -= 1

print("Sua idade é", idade)