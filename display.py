#conectando ao banco de dados-------------------
with open('database.txt','r') as banco_de_dados:
    print("",end=" ")

    for c in banco_de_dados:
        print(c,end=" ")

#----------------------------TELA----------------------------------
for grafic in range(0, 200):
    if grafic % 11 == 0:
        print(" ")
    
    elif cenario[grafic] == "#":
        print("#",end=" ")

    else:
        print(" ",end=" ")

    for cont in range(0, 4):
        if grafic == atual_form[cont]:
            print("#",end=" ")



    
    