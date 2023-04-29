def selection_sort(ls):
    for i in range(len(ls)):
        min_val_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_val_index]:
                min_val_index = j
        ls[i], ls[min_val_index] = ls[min_val_index], ls[i]
    return ls

print(selection_sort([1,3,6,9,4,3,2,0]))