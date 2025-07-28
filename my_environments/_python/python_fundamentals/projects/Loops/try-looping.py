
mahlistx2 = [["data", "0"], True, "Text", 1234]

mahlist = ["data", "0", True, "Text", 1234]

# for item in mahlist:
#     print(item)

for i in range(len(mahlist)):
    print(mahlist[i])

# dictionaries >> .keys() >> .values() or both >> items()
capitals = {
        "Washington":"Olympia",
        "California":"Sacramento",
        "Idaho":"Boise",
        "Illinois":"Springfield",
        "Texas":"Austin",
        "Oklahoma":"Oklahoma City",
        "Virginia":"Richmond"
    }

for k, v in capitals.items():
    print(k,">",v)

#print(type(capitals.values()),type(capitals.keys()),type(capitals.items()))

# let's try else in while loop
x = 0
while x < 10:
    print("the x value  is:",x)
    x += 1
    if x == 5:
        break
else: print("latest loop!! the x value  is:", x) # so the else isn't external or complementary it's part of the loop only runs after latest loop.

# let's try Finally keyword .. whether the loop was exited prematurely (e.g., using break or continue). or not?!

#m = 5
m = 0
while m < 15:
    print("the m value  is:", m)
    try:
        if m == 6:
            print(m, "..Breaked")
            m += 10
            #break #(OR)
            raise ValueError("An error occurred")
        else:
            m += 3
    except:
        continue
    finally: print("I'm from the Finally .. latest loop!!", m)
    #else: print("I'm from the else .. latest loop!!", m) it's not working if we uses the continue or break in the loop as we know

print("\n----------------------------------------------------------------------------------------\n")
for ii in range(3):
    try:
        if ii == 1:
            raise ValueError("An error occurred")
        print(f"Inside try block: {ii}")
    except ValueError as e:
        print(f"Caught exception: {e}")
    finally:
        print(f"Inside finally block for iteration {ii}")
    print(f"After try/finally block for iteration {ii}\n")
# so this is not helpful - it's not what we really neeeeed

print("\n----------------------------------------------------------------------------------------\n")
items = [1, 2, 3, 4, 5]
for idx, item in enumerate(items):
    if item == 3:
        continue
    print(f"Processing {item}")
    
    if idx == len(items) - 1:
        print("This was the last iteration")