chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    lista=[]
    for i in chunk_one:
        lista.append(i)  
    for y in chunk_two:
        lista.append(y)      
       
    return lista
    
print(merge_list(chunk_one, chunk_two))
