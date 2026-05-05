import json

dados = [
    {"nome": "João", "idade": 25, "cidade": "Curitiba"},
    {"nome": "Maria", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 28, "cidade": "Rio de Janeiro"}
]

with open('exemplo.json', 'w', encoding='utf-8' ) as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)