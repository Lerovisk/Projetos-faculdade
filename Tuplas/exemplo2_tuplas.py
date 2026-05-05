'''Exemplo de aplicação 5: Elabore um programa que crie uma tupla contendo duas listas com dados,
altere os dados da primeira lista e verifique se ocorre mudança de dados da tupla.'''

tupla = ([1, 2, 3], [4, 5, 6])

print("\n")

print(id(tupla[0])) # Mostra o local reservado na memoria RAM para esse dado

print("\n")

tupla[0].append(9)  # Adicionamos o numero 9 a primeira lista

print(tupla)

print("\n")

print(id(tupla[0]))  # Mostra o local reservado na memoria RAM para esse dado # Eh o mesmo local

'''Quando você faz tupla[0].append(9),
você alterou o conteúdo da lista,
mas perceba que o id(tupla[0]) antes e depois é o mesmo.'''

'''O local da memória do computador onde estas listas ficam permaneceu igual (vide aquele id(),
que mostra justamente isto), mas o conteúdo das listas mudou.
Por isso, o fato de alterar os dados dos objetos mutáveis da tupla não altera especificamente os dados da tupla
uma vez que ela armazena os endereços das listas, e estes endereços não mudaram.'''