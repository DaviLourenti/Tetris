a = [1,5]




#tirando valores de uma lista usando funções de string
b = [1,2,3,4,5]
b= str(b)
b = b.replace('"', '').replace(',', '').replace(' ','').replace('[','').replace(']', '')
for x in range(0, len(a)):
    b = b.replace(str(a[x]), '')
b= list(map(int,b))


#e de outra forma
c = [1,1,2,3,4,7,5]
# for x in range(0, len(a)):
#     c.remove(a[x])

# print(b)
c.sort()
c.reverse()
print(c)