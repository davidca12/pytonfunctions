"""par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
lista=par.split()

counts = []
#your code go here:
for i in lista:
    counts.append(lista.count(i))

#print(counts)

print("`Palaras\n" + str(list(zip(lista, counts))))"""
from collections import Counter

par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"


