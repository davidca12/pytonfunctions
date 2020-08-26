all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(numb):
    if numb['sexy']==True:
        return numb
            


def filter_colors(numb):
   for i in range (0,len(numb)):
       return numb['label']



resulting_names = list(filter(generate_li, all_colors))
resulting_names1 = list(map(filter_colors, resulting_names))

for i in range (0,len(resulting_names)):
    print("<li>",resulting_names1[i],"</li>")

"""no se que esta mal"""
