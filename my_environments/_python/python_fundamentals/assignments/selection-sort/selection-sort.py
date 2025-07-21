def selection_sort(input=[1,2,3,4,5]):

    n = len(input)

    for i in range(n-1):

        # assume the min value is the first unsorted one to start
        min = input[i]
        
        for j in range(i,n):  # O(n^2) # responsible to find min one and do swap
            
            if input[j] < min:
                min = input[j]
                input[i], input[j] = input[j], input[i]
                    
    return input


print(selection_sort([15,12,6,7,1,0]))
print(selection_sort([0,1,5,2,4]))
print(selection_sort([5,4,3,2,1]))
print(selection_sort([7,4,1,2,5]))
print(selection_sort())