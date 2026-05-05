import json    # Importando o json da biblioteca padrão do python.

dados = {       # Criando objtos.
    "nome": "João",
    "idade": 25,
    "cidade": "Curitiba",
    "frutas_favoritas":
        [       # Criando uma array no objeto(chave) frutas_favoritas.
        "maçã",
        "banana",
        "laranja"
        ]
}

# Gravando o JSON no arquivo
with open("example1.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

'''O dicionario 'dados' sera convertio em json, a variavel 'arquivo' irá gravar os dados,
e o parametro 'ensure_ascii'  para permitir a codificação correta de caracteres não-ASCII'''

# Lendo o JSON do arquivo
with open("example1.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo) # A variavel 'dados_lidos' vai receber traduzido para python o que tive dentro de 'arquivo' = variavel que armazenou os dados anteriormente em json
print(dados_lidos)

'''Com ensure_ascii = False, 'ã' é gravado como 'ã' '''
'''Com ensure_ascii = True,  'ã' seria gravado como '\\u00e3' '''


'''Percebeu aquele encoding=”utf-8”? Definimos este parâmetro para garantir que caracteres especiais (como o “ã” e “ç”)
sejam tratados corretamente.'''

'''Vamos escrever no arquivo JSON o dicionario "dados" e reescrever atraves da variavel arquivo,
 definimos que as ASCII devem aparecer de forma entendivel ao ser humano.'''
