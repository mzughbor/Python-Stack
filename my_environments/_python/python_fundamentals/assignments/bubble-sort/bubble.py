def bubble_sort(input=[15,12,6,7,1,0]):
    n = len(input)
    for i in range(n-1):
        # print("i >> ",i)
        for j in range(n-i-1):  # O(n^2)
            # print("j >> ",j)
            if input[j] > input[j+1]:
                input[j], input[j+1]  = input[j+1], input[j]
        # enhamncment if the inner loop didn't swap any items you can skip the rest bigger itteriations in main loop and stop.        
    return input

print(bubble_sort())

#print(bubble_sort([15,12,6,7,1,0]))
print(bubble_sort([0,1,5,2,4]))
print(bubble_sort([5,4,3,2,1]))
print(bubble_sort([7,4,1,2,5]))
