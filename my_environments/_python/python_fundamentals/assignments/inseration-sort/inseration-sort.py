def inseration_sort(input=[5,4,3,2,1]):

    n = len(input)

    for i in range(1,n):

        key = input[i]
        j = i - 1   # 0 starting point

        while j >= 0 and input[j] > key:

            input[j+1] = input[j] #shift elements to the right
            j-=1
        
        input[j+1] = key

    return input


print(inseration_sort([15,12,6,7,1,0]))
print(inseration_sort([0,1,5,2,4]))
print(inseration_sort([5,4,3,2,1]))
print(inseration_sort([7,4,1,2,5]))
print(inseration_sort())