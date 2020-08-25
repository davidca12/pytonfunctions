Celsius_values = [-2,34,56,-10]

const=32

def fahrenheit_values(x):
# the magic go here:
    l= ( x * 9 / 5) + const
    return (l)
   

   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
