
# requests.patch("https://meus-games-c0894-default-rtdb.firebaseio.com/2.json", data=info_casa)
# casa = requests.get("https://meus-games-c0894-default-rtdb.firebaseio.com/2/casa.json")

from random import choice
from msvcrt import getch 
from os import system 
                               
player_na_tela = False

cenario = []
for c in range(0, 200):
    if c > 189:
        cenario += ["#"]
    else:    
        cenario += [""]

print("      <<press start>>")

while True:
    
    if player_na_tela == False:
        t_form = [14, 15, 16, 25]    ###
        atual_form = t_form           #
        player_na_tela = True

    if cenario[atual_form[0]+10] == "#" or cenario[atual_form[1]+10] == "#" or\
    cenario[atual_form[2]+10] == "#" or cenario[atual_form[3]+10] == "#":

        cenario[atual_form[0]] = "#"
        cenario[atual_form[1]] = "#"
        cenario[atual_form[2]] = "#"
        cenario[atual_form[3]] = "#" 
        player_na_tela = False
    
    if player_na_tela == True:
        seta = getch()
    
    system('cls')

    #seta
    if seta == b'a' or seta == b'A' or seta == b'K': #ir para a esquesda
        for num in range(0, 4):
            atual_form[num] -= 1

    elif seta == b'd'or seta == b'D' or seta == b'M': #ir para a direita
        for num in range(0, 4):
            atual_form[num] += 1

    elif seta == b's'or seta == b'S' or seta == b'P': #descer mais rapido
        for num in range(0, 4):
            atual_form[num] += 10#usar acerelador de sleep(tempo)

    elif seta == b'w' or seta == b'W' or seta == b'H': #girar a forma
        if atual_form == t_form:
            peça_fixa = atual_form[1]
            peça_de_referencia = atual_form[0]                         #
                                                                      ##
            if peça_de_referencia == peça_fixa - 1 and peça_fixa > 10: #
                atual_form[0] = peça_fixa - 10
                atual_form[2] = peça_fixa - 1
                atual_form[3] = peça_fixa + 10
                                                        #
            elif peça_de_referencia == peça_fixa - 10: ###
                atual_form[0] = peça_fixa + 1       
                atual_form[2] = peça_fixa - 1
                atual_form[3] = peça_fixa - 10            
                                                      #
            elif peça_de_referencia == peça_fixa + 1: ##
                atual_form[0] = peça_fixa + 10        #
                atual_form[2] = peça_fixa + 1
                atual_form[3] = peça_fixa - 10
                
            else:                                   ###
                atual_form[0] = peça_fixa - 1        #
                atual_form[2] = peça_fixa + 1
                atual_form[3] = peça_fixa + 10

        
    #----------------------------TELA----------------------------------

    grafic = 0
    num = 0
    for y_grafic in range(0, 20):
        print(" ")
        
        for x_grafic in range(-1, 11):

            if grafic == cenario[cenario.index("#", num)]:
                print("#", end="")
                num = cenario.index("#", num)

            if x_grafic == -1 or x_grafic == 10:
                print("#", end="")

            elif grafic == atual_form[0] or grafic == atual_form[1] or\
            grafic == atual_form[2] or grafic == atual_form[3]:
                print("@",end="")
                grafic += 1
            
            else:
                print(" ", end="")
                grafic += 1
            
            

    
    