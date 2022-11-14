import json
from msvcrt import getch

while True:
    seta = getch()
    
    with open('bd.json') as file:  # recebendo valor do json
        numero = json.load(file)

    numero["numero"] += 1
        
    with open('bd.json', 'w') as fp:  # adicionando valor ao json
        json.dump(numero, fp)
    