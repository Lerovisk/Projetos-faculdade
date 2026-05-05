"""Neste caso, em vez de disparar a exceção, ela é capturada pela cláusula except,
mostrando a mensagem de “valor inválido”. Essa cláusula captura todo tipo de erro,
dando um tratamento comum independentemente de qual seja."""

try:
    num = int(input("Digite um número: "))
except:
    print("Valor inválido")


"""Neste caso, podem ser identificados vários tipos de erro, tratando cada um de forma individual."""
try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido")
except:
    print("Outro tipo de erro ocorreu!")