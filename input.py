#==================BIBLIOTECAS==================|
from random import randint, random # <-- para o NPC    ||
from random import choice # <-- para o NPC     ||
from time import sleep # <-- contador de tempo ||
from msvcrt import getch # <-- input sem enter ||
from os import system # <-- para limpar a tela ||
#===============================================|

#-------------------GERADOR-DE-FORMAS------------------------------------------------------------------
t_form = [4, 5, 6, 15]
i_form = [5, 15, 25, 35]
sqrt_form = [5, 6, 15, 16]
z_form = [4, 5, 15, 16]
l_form = [5, 15, 25, 26]

formas = ["t","i","sqrt","z","l"]

player_esta_na_tela == False
atual_form = choice(formas)
if atual_form == "t":
    atual_form = t_form

elif atual_form == "i":
    atual_form = i_form

elif atual_form == "sqrt":
    atual_form = sqrt_form

elif atual_form == "z":
    atual_form = z_form

else:
    atual_form = i_form

#------------------SETAS-------------------------------------------------------------------
seta = getch()

if seta == b'a' or seta == b'A' or seta == b'K': #ir para a esquesda
    for num in range(0, 4):
        atual_form[num] -= 1

elif seta == b'd'or seta == b'D' or seta == b'M': #ir para a direita
    for num in range(0, 4):
        atual_form[num] += 1

elif seta == b's'or seta == b'S' or seta == b'P' or seta == b'\r': #descer mais rapido
    tempo = tempo/2 #sleep(tempo) num loop ele ja volta ao normal

elif seta == b'w' or seta == b'W' or seta == b'H' or seta == b' ': #girar a forma
    if atual_form == t_form:
        peça_fixa = atual_form[1]


    elif atual_form == i_form:
        pass

    elif atual_form == z_form:
        pass

    elif atual_form == sqrt_form:
        pass

    else: #atual_form == l_form
        pass

