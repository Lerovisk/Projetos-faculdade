print("Por favor, digite tres numeros diferentes:")

#obtendo os dados

num1 = float(input("Digite o primerio numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Os números inseridos não são diferentes.")

elif num1 < num2 and num1 < num3:
    print(f"O menor numero eh: {num1}")
elif num2 < num3:
    print(f"O menor numero eh: {num2}") #se caiu aqui, o num1 eh maior que os dois
else:
    print(f"O menor numero eh: {num3}") #se caiu aqui, o num3 eh o menor



