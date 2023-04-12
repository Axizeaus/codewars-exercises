def binary_search(arr, item):
    upper_bound = arr.length - 1
    lower_bound = 0
    
    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound) / 2
        value_at_mid = arr[mid]
        
        if item == value_at_mid:
            return mid
        elif item < value_at_mid:
            upper_bound = mid - 1 
        elif item > value_at_mid:
            lower_bound = mid + 1
            
    return None