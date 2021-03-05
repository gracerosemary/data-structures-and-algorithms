def merge_sort(arr):
    n = len(arr)
    
    if n > 1:
        # mid of the array
        mid = n // 2
        # divide array into 2 halves: left and right
        left = arr[:mid]
        right = arr[mid:]
        # sort the left side 
        merge_sort(left)
        # sort the right side
        merge_sort(right)
        # merge the sorted left and right sides together
        merge(left, right, arr)
        
def merge(left, right, arr):
    # declare i (left iterator), j (right iterator), and k (array iterator) = 0
    i = j = k = 0
    
    # while left and right side is true (exists)
    while i < len(left) and j < len(right):
        # if left value is less than right value
        if left[i] <= right[j]:
            # move main iterator to the left
            arr[k] = left[i]
            # increment the left
            i += 1
        # if right value is less than the left
        else:
            # move main iterator to the right
            arr[k] = right[j]
            # increment the right
            j += 1
        # increment the main iterator
        k += 1
    
    # while the length of the left is greater than i
    while i < len(left):
        # move main iterator to the left
        arr[k] = left[i]
        # increment main and left iterator
        k += 1
        i += 1
    # while the length of the right is greater than j
    while j < len(right):
        # move main iterator to the right
        arr[k] = right[j]
        # increment main and left iterator
        k += 1
        j += 1
    
    return arr