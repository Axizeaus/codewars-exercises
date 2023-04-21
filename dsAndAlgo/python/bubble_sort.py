def bubble_sort(ls):
    unsorted_until_index = len(ls) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if (ls[i] > ls[i+1]):
                ls[i], ls[i+1] = ls[i+1], ls[i]
                sorted = False
        unsorted_until_index -= 1
    return ls

print(bubble_sort([2,3,5,1,6,2,3,7]))