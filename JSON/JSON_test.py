import json

PI = 1.1314
nome = "Leticia"

hardware_fav = {
    "ano_aquisicao" : 2025,
    "processador" : "Intel Core Ultra",
    "memoria_gb" : 32,
    "cor" : "preta",

    #Lista de dicionarios
    "perifericos" : [
        {
        "tipo" : "teclado",
        "marca" : "logitéc",
        },

        {
        "tipo" : "manche de avião",
        "marca" : "trustmaster"
        },

        {
        "tipo" : "Volante",
        "marca" : "logitéc"
        }
    ]
}
with open("test.json", "w", encoding= 'UTF - 8') as json_file:
    json.dump(hardware_fav, json_file)

with open("test.json", "r",encoding= 'UTF - 8') as json_file:
    dicionario_lido = json.load(json_file)

for key, value in dicionario_lido.items():
    if key == "perifericos":
        print(f"{key}:")
        for periferico in value:           # cada item é um dicionário
            for title, attr in periferico.items():   # aí sim desempacota
                print(f"  {title} : {attr}")
    else:
        print(f"{key} : {value}")

'''in pickle:
with open('pickle_file', 'wb') as arquivo:
    pickle.dump([hardware_fav, PI, nome], arquivo)

hardware_fav_lido, PI_lido, nome_lido = pickle.load(open('pickle_file', 'rb'))
print(hardware_fav_lido)
print(PI_lido)
print(nome_lido)
'''