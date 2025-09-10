#Biggie Size
def biggie_size(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

print(biggie_size([-1, 3, 5, -5]))

print("\n----------------------------------------------------------------------------------------\n")

#Count Positives
def count_positives(list):
    count = 0
    for num in list:
        if num > 0:
            count += 1
    list[-1] = count
    return list

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

print("\n----------------------------------------------------------------------------------------\n")

#Sum Total
def sum_total(list):
    total = 0
    for num in list:
        total += num
    return total

print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))

print("\n----------------------------------------------------------------------------------------\n")

#Average
def average(list):
    length = len(list)
    if length == 0:
        print("Empty list, please enter vaild list")
        return None
    total = 0
    for num in list:
        total += num
    return total / length

print(average([1, 2, 3, 4]))
print(average([10]))
print(average([]))

print("\n----------------------------------------------------------------------------------------\n")

#Length
def length(list):
    count = 0
    for i in list:
        count += 1
    return count

print(length([37, 2, 1, -9]))
print(length([]))

print("\n----------------------------------------------------------------------------------------\n")

#Minimum
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min_value = list[0]
        for num in range(1,len(list)):
            if list[num] < min_value:
                min_value = list[num]
        return min_value

print('Minimum')
print(minimum([37, 2, 1, -9]))
print(minimum([]))
print(minimum([5]))
print(minimum([1,4,5]))
print(minimum([5,4,5,6]))

print("\n----------------------------------------------------------------------------------------\n")

#Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max_value = list[0]
        for num in range(1,len(list)):        
            if list[num] > max_value:
                max_value = list[num]
        return max_value

print('Maximum')
print(maximum([37, 2, 1, -9]))
print(maximum([]))
print(maximum([5]))
print(maximum([1,40,5]))
print(maximum([5,4,5,6]))

print("\n----------------------------------------------------------------------------------------\n")

#Ultimate Analysis
def ultimate_analysis(list):
    len = length(list)
    if len == 0:
        return False
    else:
        sum = sum_total(list)
        avg = average(list)
        min = minimum(list)
        max = maximum(list)
    
    return {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length':len
    }

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([1, 2, 3, 4]))
print(ultimate_analysis([]))
print(ultimate_analysis([1]))



print("\n----------------------------------------------------------------------------------------\n")

#Reverse List
def reversedList(list):
    lenList = len(list)
    for i in range(lenList): # I said i in range not item in list this important.
        print("Loop number:", i+1) # I have to loop in all elemnts in the given array in this solustion.
        list.insert(0, list[i+i]) # the other i is insted of using new same values variable about counting the adds as counter...
    return list[:lenList] # trim extra elements you don't need.

print([5,6,7,8,-1])
print(reversedList([5,6,7,8,-1]))

# Explaination for my idea ... in each round we have new elemnts added right!?
# >>> 0 >> 0 >> list[0] >> [5, 6, 7, 8, -1]  we didn't added any new element yet same array right.
# >>> 1 >> 2 >> list[2] >> [5, 5, 6, 7, 8, -1] after adding first one
# >>> 2 >> 4 >> list[4] >> [6, 5, 5, 6, 7, 8, -1] now the pattern become clear
# >>> 3 >> 6 >> list[6] >> [7, 6, 5, 5, 6, 7, 8, -1] 
# >>> 4 >> 8 >> list[8] >> [8, 7, 6, 5, 5, 6, 7, 8, -1]
# >>> 5 > 10 > list[10] >> [-1, 8, 7, 6, 5, 5, 6, 7, 8, -1] now you can apply your triming shape you neeed
# >>> len / execluding it in range we started from 0

print("\n----------------------------------------------------------------------------------------\n")

# Another idea is better with half time complexcity case you loop on half array... using pointers idea...

def reverse_list_in_place(input_list):

    """
    The idea is all about swaping elements while looping until reaching the middle elemnt..
    """

    left = 0
    right = len(input_list) - 1

    while left < right: 
        #print("left :", left, "right :", right) /// I have  7 elements i only looped 3 times
        print("Loop number:", left+1)
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1       
        right -= 1
    return input_list

print([11,22,33,44,55,66,77])
print(reverse_list_in_place([11,22,33,44,55,66,77]))