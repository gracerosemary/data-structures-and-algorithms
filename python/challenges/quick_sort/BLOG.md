# Quick Sort
Quick Sort is a sorting algorithm. Given an array, the algorithm takes the values of the array and places them in the correct position. 
____
## Psuedo Code
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
____
## Trace
Sample Array: `[8,4,23,42,16,15]`

arr = [8,4,23,42,16,15]  

**Original Array:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 8 | 4 | 23 | 42 | 16 | 15 | 

|-ONE-------------- **Partition(arr, left, right):** -------------------|  

**Starting Postitions:**  
left: 0  
    - lowest index
right: 5
    - highest index  
pivot: arr[right] --> arr[5] --> 15

**Initialize index of smaller element (low):**  
low: (left-1) --> (0-1) --> -1  

**Traverse elements from left to right:**  
index: 0   
> If arr[i] <= pivot:
- Is 8 <= 15? 
    - Yes. Increment `low` and then `swap(arr, i, low)`

low: (-1 + 1) --> 0

|-TWO------------------- **Swap(arr, i, low):** ----------------------|  

1. temp = 0  
2. temp = arr[i]  
    - temp = 8  
3. arr[i] = arr[low]
    - arr[i] = 8 
4. arr[low] = temp
    - arr[low] = 8

** No changes to the array because arr[i] and arr[low] are the same

|-THREE-------------- **Partition(arr, left, right):** ------------------|  

index: 1  
- Is 4 <= 15? 
    - Yes. Increment `low` and then `swap(arr, i, low)`

low: (0 + 1) --> 1    

|-FOUR-------------------- **Swap(arr, i, low):** ----------------------|

1. temp = 0  
2. temp = arr[i]  
    - temp = 4  
3. arr[i] = arr[low]
    - arr[i] = 4 
4. arr[low] = temp
    - arr[low] = 4

** No changes to the array because arr[i] and arr[low] are the same

|-FIVE-------------- **Partition(arr, left, right):** ---------------------|  

index: 2  
- Is 23 <= 15? 
    - No. Do nothing.  

|-SIX-------------- **Partition(arr, left, right):** ----------------------|  

index: 3    
- Is 42 <= 15? 
    - No. Do nothing.  

|-SEVEN-------------- **Partition(arr, left, right):** -------------------|  

index: 4  
- Is 16 <= 15? 
    - No. Do nothing.   

|-EIGHT--------------- **Partition(arr, left, right):** -------------------|  

index: 5  
- Is 15 <= 15? 
    - Yes. Increment `low` and then `swap(arr, i, low)`   

low: (1 + 1) --> 2       

1. temp = 0  
2. temp = arr[i]  
    - temp = 15    
3. arr[i] = arr[low]
    - arr[i] = 2    
4. arr[low] = temp
    - arr[low] = 15  


|-NINE------------------- **Swap(arr, right, low+1):** --------------------|

**Current Postitions:**  
right: 5  
low: (1 + 1) --> 2  

`swap(arr, 5, 2)`

**New Array after swapping position 2 and 5:**

| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 8 | 4 | 15 | 42 | 16 | 23 | 

**Return low + 1:**  
low + 1 --> 1 + 1 --> 2   
    - this value is `part`  

|-TEN------------------ **Quick Sort(arr, left, right):** --------------------|  
**Current Postitions:**    
left: 0    
right: 5     
part: 2   

Since left < right:
part: 2    

|-ELEVEN-------------- **Quick Sort(arr, left, part-1):** --------------------|  
**Current Postitions:**    
left: 0    
right(or part-1): 1  

Since left < part-1:
go through partition  

|-TWELVE-------------- **Partition(arr, left, right):** ------------------------|  

**Starting Postitions:**  
left: 0  
right: 1  
pivot: 4  

**Initialize index of smaller element (low):**  
low: -1  

**Traverse elements from left to right:**  
index: 0   
> If arr[i] <= pivot:
- Is 8 <= 15? 
    - Yes. Increment `low` and then `swap(arr, i, low)`

low: (-1 + 1) --> 0

|----------------------------**REPEATING-STEPS**--------------------------|  
Repeat steps 2-10 until all elements in list have been iterated through partition and swap. 

**Resulting Arrays:**  

**Swapping position 1 & 2**:  
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 42 | 16 | 23 | 

**Swapping position 3 & 4**:  
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 16 | 42 | 23 | 

**Swapping position 4 & 5**:  
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 16 | 23 | 42 |  

|--------------------------------**FINAL-ARRAY**-----------------------------|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 16 | 23 | 42 |  

_____
## Efficiency
Big O Time: O(n*2)  
Big O Space: O(log(n))    





