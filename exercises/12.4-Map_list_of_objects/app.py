import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(person):
    
    today = datetime.date.today()
    

    age = today.year - person['birthDate'].year - ((today.month, today.day) < (person['birthDate'].month, person['birthDate'].day))
    
    return age

name_list = list(map(lambda person:  person["name"] , people))
otra_list = list(map(calculateAge , people))

for i in range (0,len(people)):
    print('Hello, my name is', name_list[i], 'I am ',otra_list[i],'years old !!')



