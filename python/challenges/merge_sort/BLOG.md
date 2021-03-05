# Merge Sort

Sorts an array from smallest to largest.
____
## Psuedo Code
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```
____
## Trace for left side (repeat passes for the same logic on the right side)
Sample Array: `[8,4,23,42,16,15]`

### Pass 1:
arr = [8,4,23,42,16,15]

**Original List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 8 | 4 | 23 | 42 | 16 | 15 | 

> merge_sort(arr):  
n = 6  
mid = 3  

**Left:**
| Index | 0 | 1 | 2 | 
| ----- | - | - | - | 
| Value | 8 | 4 | 23 | 

**Right:**
| Index | 0 | 1 | 2 |  
| ----- | - | - | - | 
| Value | 42 | 16 | 15 | 

____
### Pass 2:
arr = [8,4,23]

> merge_sort(arr):  
n = 3  
mid = 1   

**Left:**
| Index | 0 | 
| ----- | - | 
| Value | 8 | 

**Right:**
| Index | 0 | 1 | 
| ----- | - | - | 
| Value | 4 | 23 | 

____
### Pass 3:
arr = [8]

> merge_sort(arr):  
n = 1 
 
n is not greater than 1. Because condition is not met, we go back to sorting the right
____
### Pass 4:
arr = [4,23]  

> merge_sort(arr):  
n = 2   
mid = 1   

**Left:**
| Index | 0 | 
| ----- | - | 
| Value | 4 | 

**Right:**
| Index | 0 |
| ----- | - | 
| Value | 23 |

*The last element on the right/left will continue to not meet the initial condition of being greater than 1, so Pass #3 will repeat for all last elements in an array.
___
### Pass 5:

> merge(left, right, arr):  
i = 0  
j = 0  
k = 0  

**Arr:**
| Index | 0 | 1 | 
| ----- | - | - | 
| Value | 4 | 23 | 

**Left:**
| Index | 0 | 
| ----- | - | 
| Value | 4 | 

**Right:**
| Index | 0 |
| ----- | - | 
| Value | 23 |

> Condition 1: Is i < len(left) and j < len(right)?  
Yes, 0 is smaller than 1 and 0 is smaller than 1  

> Condition 2: Is left[i] <= right[j]?  
Yes, 4 is smaller than 23.   

> Condition 2 met: increment i by 1  
i = 1  

> Increment k after Condition 1 is finished  
k = 1  

> Condition 3: Is i < len(left)?  
No, 1 is not smaller than 1.  

> Condtion 4: Is j < len(right)?  
Yes, 0 is smaller than 1.  

> Condition 4 met: increment k and i:  
i = 2  
k = 2  
j = 0  

**Sorted Merge:**
| Index | 0 | 1 | 
| ----- | - | - | 
| Value | 4 | 23 | 

*merge continues by combining all the previously split arrays:  
**Final Sorted Merge:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 16 | 23 | 42 | 
_____
## Efficiency
Big O Time: O(n*log(n)) || T(n) = 2 * T(n / 2) + O(n)  
Big O Space: O(n)  
____