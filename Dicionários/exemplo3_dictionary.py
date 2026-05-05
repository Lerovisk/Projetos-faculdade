agenda = {"Maria": "(41) 98765-4321",
          "João": "(11) 12345-6789"}

print("Agenda antes: ")
for contato, valor in agenda.items():
    print(f"{contato}: {valor}")

print("\nQuando o valor existe e usamos .pop(): ")
print(agenda.pop("Maria"))   # Retorna o que foi removido

print("\nQuando o valor nao existe: ")
print(agenda.pop("José", "Contato com nome José não localizado.\n"))   # Retorna uma mensagem informando sua ausencia

print("Agenda atual: ")
for contato, valor in agenda.items():
    print(f"{contato}: {valor}")