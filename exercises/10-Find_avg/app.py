my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
aux=0
longitud=len(my_list)

for i in range (0,len(my_list)):
    aux+=my_list[i]

total=aux/longitud

print (total)


