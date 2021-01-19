def FindMid(sorted_array, search_key):
    low = 0
    high = len(sorted_array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2 
        if  search_key > sorted_array[mid]:
            low = mid + 1
        elif search_key < sorted_array[mid]:
            high = mid - 1
        else:
            return mid
    else:
        return -1

def BinarySearch(sorted_array, search_key):
    index = FindMid(sorted_array, search_key)
    if index != -1:
        return index
    else: 
        return -1