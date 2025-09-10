print("\n--1-------------------------------------------------------------------------------------\n")

def countdown(int):
    result = []
    for i in range(int,-1,-1):
        result.append(i)
    return result

print(">>> countdown :",countdown(5))

print("\n--2-------------------------------------------------------------------------------------\n")

def print_and_return(input):
    if not isinstance(input, list) or len(input) != 2 or not all(isinstance(i, int) for i in input):
        print("Argument must be a list containing only two numbers.")
        return None
    else:
        print(input[0])
        return(input[1])
    
print(">>> print_and_return")
print_and_return([1,2])
print_and_return(["1","4"])

print("\n--3-------------------------------------------------------------------------------------\n")

def first_plus_length(input):
    if isinstance(input, list) and isinstance(input[0],int):
        return len(input)+input[0]
    else:
        print("Please inter only a list! Contaning int's")
        return None

print(">>> first_plus_length:", first_plus_length([3,3]))

print("\n--4-------------------------------------------------------------------------------------\n")

def values_greater_than_second(input): 
    output = []
    if isinstance(input, list) and len(input) > 2:
        for i in input:
            if i > input[1]:
                output.append(i)
        return output
    else:
        print("The input should be List type and having more that two values")
        return False

print(">>> values_greater_than_second :")
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5,5,5,6,7,4]))
print(values_greater_than_second([5,2]))
print(values_greater_than_second([5,1,2]))

print("\n--5-------------------------------------------------------------------------------------\n")

def length_and_value(*ints):
    length, value = ints
    if isinstance(length, int) and isinstance(value, int) and len(ints) == 2:
        return [value] * length
    else:
        print("Both arguments must be exactly two integers.")
        return False

print(">>> length_and_value :")
print(length_and_value("4",7))
print(length_and_value("4","7"))
print(length_and_value(4,"7"))
print(length_and_value(1,2))
print(length_and_value(6,5))
print(length_and_value(9,0))
print(length_and_value(0,9))
