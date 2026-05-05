# Se a minha idade for maior que a do meu primo, escreva uma mensagem afirmando isso.
# Senão, mostre uma mensagem afirmando que ele  é mais velho do que eu.
# Se a minha idade for igual a do meu primo então escreva uma mensagem afirmando que temos a mesma idade.


minha_idade = input("Qual a sua idade? ")
idade_do_meu_primo = input("Qual a idade do seu primo? ")

if minha_idade > idade_do_meu_primo:
    print("Você é o mais velho!")

elif minha_idade < idade_do_meu_primo:
    print("Ele é o mais velho!")

else:
    print("Vocês dois tem a mesma idade!")
