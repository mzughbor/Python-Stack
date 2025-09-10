import random

def randInt(min=None, max=None):

    # Default Status: 0 - 100
    if min is None and max is None:
        min = 0
        max = 100
    
    # Only max is given
    elif min is None:
        min = 0
    
    # Only min is given
    elif max is None:
        max = 100
    
    # BONUS check if
    if min > max:
        #print("Swaping min and max")
        min, max = max, min

    # Generate the random float, convert it to int range 
    num = random.random() * (max-min) + min
    return round(num)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=500, max=50))
