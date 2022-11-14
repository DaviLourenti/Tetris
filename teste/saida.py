import json
from os import O_SEQUENTIAL, system 
        

while True:
    with open('bd.json') as file:  # recebendo valor do json
        numero_orig = json.load(file)

    while True:

        with open('bd.json') as file:  # recebendo valor do json
            numero_novo = json.load(file)

        if numero_orig != numero_novo:
            system('cls')
            print(numero_novo["numero"])
            break
    