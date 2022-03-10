#conectando ao banco de dados-------------------

#with open('database.txt','r') as banco_de_dados:
#    print("",end=" ")
#
#    for c in banco_de_dados:
#        print(c,end=" ")
from random import choice
from msvcrt import getch 
from os import system 
                                #  ##      ## #
t_form = [4, 5, 6, 15]     ###  #  ##     ##  #    #
i_form = [5, 15, 25, 35]    #   #      ##     ##   #
sqrt_form = [4, 5, 14, 15]      #       ##        ##
z_form_1 = [4, 5, 15, 16]           
z_form_2 = [5, 6, 14, 15]      
l_form_1 = [5, 15, 25, 26]        
l_form_2 = [5, 15, 24, 25]      

formas = ["t","i","sqrt","z1","l1","z2","l2"]
atual_form = choice(formas)

if atual_form == "t":
    atual_form = t_form

elif atual_form == "i":
        atual_form = i_form

elif atual_form == "sqrt":
    atual_form = sqrt_form

elif atual_form == "z1":
    atual_form = z_form_1

elif atual_form == "z2":
    atual_form = z_form_2

elif atual_form == "l2":
    atual_form = l_form_1

else:
    atual_form = i_form

while True:

    seta = getch()
    system('cls')

    

    #seta
    if seta == b'a' or seta == b'A' or seta == b'K': #ir para a esquesda
        for num in range(0, 4):
            atual_form[num] -= 1

    elif seta == b'd'or seta == b'D' or seta == b'M': #ir para a direita
        for num in range(0, 4):
            atual_form[num] += 1

    elif seta == b's'or seta == b'S' or seta == b'P' or seta == b'\r': #descer mais rapido
        pass
        #tempo = tempo/2 #sleep(tempo) num loop ele ja volta ao normal

    elif seta == b'w' or seta == b'W' or seta == b'H' or seta == b' ': #girar a forma
        pass
    #----------------------------TELA----------------------------------

    grafic = 0
    t_form = [4, 5, 6, 15]

    for y_grafic in range(0, 20):
        print(" ")
        
        for x_grafic in range(-1, 11):
            if x_grafic == -1 or x_grafic == 10:
                print("#", end="")

            elif grafic == atual_form[0] or grafic == atual_form[1] or\
            grafic == atual_form[2] or grafic == atual_form[3]:
                print("@",end="")
                grafic += 1
            
            else:
                print(" ", end="")
                grafic += 1
            
            

    
    