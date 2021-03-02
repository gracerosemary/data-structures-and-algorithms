# Insertion Sort
Insertion Sort is a sorting algorithm. Given an array, the algorithm takes the values of the array and places them in the correct position. 
____
## Algorithm
- InsertionSort is a method that sorts the values in an array, in ascending order. It takes in an array of integers.
- Iterate, starting at index 1 through the length of the array.
- Compare the current int to the previous int.
- If the current int is less than the previous int, compare it to the ints that come before the previous int.
- Move the int with the bigger value to the next index position so that it can be swapped with the int of smaller value.
____
## Psuedo Code
```
 InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <— temp
```
____
## Trace
Sample Array: `[8,4,23,42,16,15]`

### Pass 1:
int_arr = [8,4,23,42,16,15]

**Original List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 8 | 4 | 23 | 42 | 16 | 15 | 

```
int_arr[j+1] = int_arr[j]
# int_arr[0+1] = int_arr[0]
# int_arr[1] = int_arr[0]
# index 0 will hold the same value as index 1
```
> variables + current values:   
i = 1  
j = 0   
temp = 4   

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 8 | 8 | 23 | 42 | 16 | 15 | 

```
j -= 1
```

> variables + current values:   
i = 1  
j = -1  
temp = 4 

**Ending List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 

____
### Pass 2:
int_arr = [4,8,23,42,16,15]

**Original List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 

> variables + current values:   
i = 2  
j = 1   
temp = 23   

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 

> variables + current values:   
i = 2    
j = 1   
temp = 23   

**Ending List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 
____
### Pass 3:
int_arr = [4,8,23,42,16,15]

**Original List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 

> variables + current values:   
i = 3  
j = 2   
temp = 42   

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 

> variables + current values:   
i = 3   
j = 2    
temp = 42    

**Ending List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 
____
### Pass 4:
int_arr = [4,8,23,42,16,15]

**Original List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 16 | 15 | 

> variables + current values:   
i = 4  
j = 3    
temp = 16   

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 42 | 42 | 15 | 

> variables + current values:   
i = 4     
j = 2        
temp = 16      

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 23 | 23 | 42 | 15 | 

> variables + current values:   
i = 4     
j = 1          
temp = 16      

**Ending List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 16 | 23 | 42 | 15 | 
___
### Pass 5:
int_arr = [4,8,16,23,42,15]

**Original List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 16 | 23 | 42 | 15 | 

> variables + current values:   
i = 5    
j = 4        
temp = 15    

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 16 | 23 | 42 | 42 | 

> variables + current values:   
i = 5      
j = 3          
temp = 15        

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 16 | 23 | 23 | 42 | 

> variables + current values:   
i = 5       
j = 2          
temp = 15   

**New List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 16 | 16 | 23 | 42 | 

> variables + current values:   
i = 5       
j = 1            
temp = 15   

**Ending List:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 16 | 23| 42 | 
___
### Pass 6 (printing out values):
```
for i in range(len(int_arr)):
  print(int_arr[i])
```
| Index | 0 | 1 | 2 | 3 | 4 | 5 |  
| ----- | - | - | - | - | - | - |  
| Value | 4 | 8 | 15 | 16 | 23| 42 | 
| Print | 4 | - | - | - | - | - | 
| Print | 4 | 8 | - | - | - | - | 
| Print | 4 | 8 | 15 | - | - | - | 
| Print | 4 | 8 | 15 | 16 | - | - | 
| Print | 4 | 8 | 15 | 16 | 23 | - | 
| Print | 4 | 8 | 15 | 16 | 23 | 42 | 


_____
## Efficiency
Big O Time: O(n*2)  
- Worst case scenario, integers are sorted in reverse order, which would take the max time.
- Best case scenario, Big O would be O(1) because the array is already sorted.

Big O Space: O(1)
- Same number of pointers used, regardless of list size
____
## Sorting.at - Insertion Sort Visual
![insertion sort visual](/python/assets/insertsort.png)



