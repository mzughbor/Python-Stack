def selection_sort(input=[1,2,3,4,5]):

    n = len(input)
    for i in range(n):
        
        # assume the min value is the first one to start
        min_index = i
        for j in range(i+1,n):  # O(n^2) # responsible to find min one
            if input[j] < input[min_index]:                
                min_index = j
            
        if min_index != i:

            input[i], input[min_index] = input[min_index], input[i]

    return input


print(selection_sort([15,12,6,7,1,0]))
print(selection_sort([0,1,5,2,4]))
print(selection_sort([5,4,3,2,1]))
print(selection_sort([7,4,1,2,5]))
print(selection_sort())