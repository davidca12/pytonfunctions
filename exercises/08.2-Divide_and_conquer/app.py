list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(list1):
    #Your code go here:
    lista=[]
    listas1=[]
    lista3=[]

    
    for i in list1:
        if i%2==0:
            listas1.append(i)
        else:
            lista.append(i)
    lista3.append(lista)
    lista3.append(listas1)
    

       
    return lista3


print(merge_two_list(list_of_numbers))

