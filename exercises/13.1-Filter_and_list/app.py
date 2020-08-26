
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def my_function(numb):
    for i in range (0,len(numb)):
        re=numb[i].find("R") 
        if re!=-1:
            return numb[i]
        

resulting_names = list(filter(my_function, all_names))

print(resulting_names)





