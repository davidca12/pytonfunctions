import random
#Remember import random function here:


my_list = [4,5,734,43,45]

#The magic is here:

def generate_random_list():
    aux_list = []
    

    for i in range(10):
        randonlength = random.randint(0,10)
        aux_list.append(randonlength)
        i += i
    return aux_list
my_stupid_list = my_list+generate_random_list()


print(my_stupid_list)