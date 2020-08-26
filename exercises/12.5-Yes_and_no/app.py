theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def mapeo(der):
    if der==1:
        return 'wiki'
    elif der==0:
        return 'woko'

lista=list(map(mapeo,theBools))
print(lista)



