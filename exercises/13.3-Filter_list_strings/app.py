
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']


#Your code go here:
def my_function(numb):
        dar= 'am' in numb
        if dar==True:
            return numb
        



resulting_names = list(filter(my_function, names))

print(resulting_names)


    """for i in range (len(numb)): filter va de una en una entonces.
        re=numb[i].find("am")
        if re!=-1 :
            return numb"""
  
   