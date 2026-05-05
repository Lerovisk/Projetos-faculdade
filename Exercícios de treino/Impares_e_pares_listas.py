'''Exemplo de aplicação 2: Elabore um programa que solicite ao usuário cinco números
e exiba duas listas separadas: uma contendo somente números pares e outra contendo somente números ímpares. '''

# Caso queiramos adicionar novos itens à lista, ela irá iniciar vazia:
pares = []  # Lista de numeros pares
impares = [] # Lista de numeros ímpares

print("Digite 5 números, diremos se são pares ou ímpares")
for i in range(5): # Vai se repetir cinco vezes (de 0 a 4).
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        pares.append(num) #Vai adicionar um novo número par
    else:
        impares.append(num) #Vai adicionar um novo número ímpar

# Mostra os numeros adicionados as duas listas.
print(f"Numeros pares: {pares}, Numeros impares: {impares}")