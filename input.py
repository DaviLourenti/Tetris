#==================BIBLIOTECAS==================|
from random import randint, random # <-- para o NPC    ||
from random import choice # <-- para o NPC     ||
from time import sleep # <-- contador de tempo ||
from msvcrt import getch # <-- input sem enter ||
from os import system # <-- para limpar a tela ||
#===============================================|

#-----------------valores-iniciais-------------------------------------------------------------------

player_ta_na_tela = False

#------------------LOOP-INFINITO----------------------------------------------------------------------

while True:

#-------------------GERADOR-DE-FORMAS------------------------------------------------------------------
                                    #  ##      ## #
    t_form = [4, 5, 6, 15]     ###  #  ##     ##  #    #
    i_form = [5, 15, 25, 35]    #   #      ##     ##   #
    sqrt_form = [5, 6, 15, 16]      #       ##        ##
    z_form_1 = [4, 5, 15, 16]           
    z_form_2 = [5, 6, 14, 15]      
    l_form_1 = [5, 15, 25, 26]        
    l_form_2 = [5, 15, 24, 25]       

    formas = ["t","i","sqrt","z1","l1","z2","l2"]

    if player_ta_na_tela == False:
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
            pe??a_fixa = atual_form[1]
            pe??a_de_referencia = atual_form[0]                         #
                                                                      ##
            if pe??a_de_referencia == pe??a_fixa - 1 and pe??a_fixa > 10: #
                atual_form[0] = pe??a_fixa - 10
                atual_form[2] = pe??a_fixa - 1
                atual_form[3] = pe??a_fixa + 10
                                                        #
            elif pe??a_de_referencia == pe??a_fixa - 10: ###
                atual_form[0] = pe??a_fixa + 1       
                atual_form[2] = pe??a_fixa - 1
                atual_form[3] = pe??a_fixa - 10            
                                                      #
            elif pe??a_de_referencia == pe??a_fixa + 1: ##
                atual_form[0] = pe??a_fixa + 10        #
                atual_form[2] = pe??a_fixa + 1
                atual_form[3] = pe??a_fixa - 10
                
            else:                                   ###
                atual_form[0] = pe??a_fixa - 1        #
                atual_form[2] = pe??a_fixa + 1
                atual_form[3] = pe??a_fixa + 10

        elif atual_form == i_form:
            pe??a_fixa = atual_form[2]
            pe??a_de_referencia = atual_form[0]                         
                                                     # # # #
            if pe??a_de_referencia == pe??a_fixa - 20: 
                atual_form[0] = pe??a_fixa - 2
                atual_form[1] = pe??a_fixa - 1
                atual_form[3] = pe??a_fixa + 1          #
                                                       #
            else:                                      #
                atual_form[0] = pe??a_fixa - 20         #
                atual_form[1] = pe??a_fixa - 10
                atual_form[3] = pe??a_fixa + 10          

        elif atual_form == z_form_1:
            pe??a_fixa = atual_form[1]
            pe??a_de_referencia = atual_form[0]                          #
                                                                       ##
            if pe??a_de_referencia == pe??a_fixa - 1 and pe??a_fixa > 10: #
                atual_form[0] = pe??a_fixa - 10
                atual_form[2] = pe??a_fixa - 1
                atual_form[3] = pe??a_fixa + 9
                                                           
            else:                                   ##
                atual_form[0] = pe??a_fixa - 1        ##
                atual_form[2] = pe??a_fixa + 10
                atual_form[3] = pe??a_fixa + 11
        
        elif atual_form == z_form_2:
            pe??a_fixa = atual_form[0]
            pe??a_de_referencia = atual_form[1]                         # 
                                                                       ##
            if pe??a_de_referencia == pe??a_fixa + 1 and pe??a_fixa > 10:  #
                atual_form[1] = pe??a_fixa + 10
                atual_form[2] = pe??a_fixa - 1
                atual_form[3] = pe??a_fixa + 9
                                                           
            else:                                     ##
                atual_form[1] = pe??a_fixa + 1        ##
                atual_form[2] = pe??a_fixa + 9
                atual_form[3] = pe??a_fixa + 10

        elif atual_form == l_form_1:
            pe??a_fixa = atual_form[1]
            pe??a_de_referencia = atual_form[0] 
                                                                        ###
            if pe??a_de_referencia == pe??a_fixa - 10 and pe??a_fixa > 10: #
                atual_form[0] = pe??a_fixa + 1
                atual_form[2] = pe??a_fixa - 1
                atual_form[3] = pe??a_fixa + 9
                                                       ## 
            elif pe??a_de_referencia == pe??a_fixa + 1:   #
                atual_form[0] = pe??a_fixa + 10          #
                atual_form[2] = pe??a_fixa - 10
                atual_form[3] = pe??a_fixa - 9            
                                                         #
            elif pe??a_de_referencia == pe??a_fixa + 10: ###
                atual_form[0] = pe??a_fixa - 1          
                atual_form[2] = pe??a_fixa + 1
                atual_form[3] = pe??a_fixa - 11
                                                      #
            else:                                     #
                atual_form[0] = pe??a_fixa - 10        ##
                atual_form[2] = pe??a_fixa + 10       
                atual_form[3] = pe??a_fixa + 11
        
        elif atual_form == l_form_2:
            pe??a_fixa = atual_form[1]
            pe??a_de_referencia = atual_form[0] 
                                                                        #
            if pe??a_de_referencia == pe??a_fixa - 10 and pe??a_fixa > 10: ###
                atual_form[0] = pe??a_fixa + 1                           
                atual_form[2] = pe??a_fixa - 9
                atual_form[3] = pe??a_fixa - 1
                                                        ##
            elif pe??a_de_referencia == pe??a_fixa + 1:   #
                atual_form[0] = pe??a_fixa + 10          #
                atual_form[2] = pe??a_fixa - 11
                atual_form[3] = pe??a_fixa - 10            
                                                      
            elif pe??a_de_referencia == pe??a_fixa + 10: ###
                atual_form[0] = pe??a_fixa - 1            #
                atual_form[2] = pe??a_fixa + 11
                atual_form[3] = pe??a_fixa + 1
                
            else:                                     #
                atual_form[0] = pe??a_fixa - 10        #
                atual_form[2] = pe??a_fixa + 9        ## 
                atual_form[3] = pe??a_fixa + 10

        else: # atual_form == sqrt_form        ##
            pass                               ##
            

