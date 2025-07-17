print("\n----------------------------------------------------------------------------------------\n")
#Reverse List
def reversedList(list):
    lenList = len(list)
    for i in range(lenList):        
        list.insert(0, list[i+i]) # the other i is insted of using new same vlues variable about counting the adds...
    return list[:lenList]

print(reversedList([5,6,7,8,-1]))

print("\n----------------------------------------------------------------------------------------\n")
# other idea is better with half time complexcity...
def reverse_list_in_place(input_list):

    left = 0
    right = len(input_list) - 1
    #flag = 0

    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1        
        right -= 1
        #flag += 1
    #print(input_list, "Flag is :",flag)
    return input_list

print(reverse_list_in_place([11,22,33]))