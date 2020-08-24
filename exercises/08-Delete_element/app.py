people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    people1=[]
    for i in people:        
       if person_name!=i:
           people1.append(i)
    return people1       
           

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))