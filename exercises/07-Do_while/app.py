
#Your code go here:
x = 20
while x >= -1:
    if x < 0:
        print("LIFTOFF")
        x -=1 
    elif x%5 == 0:
        print(x,"!")
        x -=1
    elif x%5 != 0:
        print(x)
        x -=1