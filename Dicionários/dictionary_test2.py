agenda = {
          "Maria": "(41) 98765-4321",
          "João": "(11) 12345-6789",
          "Rosana": "(21) 91827-3645"
          }

for chave, valor in agenda.items():
    print(f"{chave}: {valor}")

print("-"*40)

# Adiciona um novo elemento no vetor/dicionario
agenda["José"] = "(19) 98877-1122"

for chave, valor in agenda.items():
    print(f"{chave}: {valor}")

print("-"*40)

# Cria um dicionário com chaves e valores específicos
chaves = ["chave1", "chave2", "chave3"]
valores = "valor"
novo_dicionario = dict.fromkeys(chaves, valores) # Novo dicionario, com chaves e valores especificos

for chave, valor in novo_dicionario.items():
    print(f"{chave}: {valor}")

print("-"*40)

# mostra a lista de itens do dicionário
print(agenda.items())

print("-"*40)

# mostra a lista de chaves do dicionário
print(agenda.keys())

print("-"*40)

# mostra a lista de valores do dicionário
print(agenda.values())

print("-"*40)

# remove um item de chave específica
agenda.pop("Maria")
for chave, valor in agenda.items():
    print(f"{chave}: {valor}")

print("-"*40)

# remove o último item inserido (Jose)
agenda.popitem()
for chave, valor in agenda.items():
    print(f"{chave}: {valor}")

print("-"*40)

# retorna ou insere o valor de uma chave em específico
print(agenda.setdefault("Rosana", "(21) 91827-3645"))
print(agenda.setdefault("Maria", "(41) 98765-4321"))
print(agenda.setdefault("Pedro", "(41) 000000000"))
print("Novo item adicionado")
for chave, valor in agenda.items():
    print(f"{chave}: {valor}")

print("-"*40)

# adiciona o conteúdo de um dicionário a outro
agenda.update(novo_dicionario)

for chave, valor in agenda.items():
    print(f"{chave}: {valor}")

print("-"*40)

# limpa o conteúdo de um dicionário
agenda.clear()
print(agenda)       

