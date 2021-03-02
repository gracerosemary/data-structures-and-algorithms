def insertion_sort(int_arr):
  for i in range(1, len(int_arr)):
    j = i -1
    temp = int_arr[i]
    while j >= 0 and temp < int_arr[j]:
      int_arr[j+1] = int_arr[j]
      j -= 1
    int_arr[j+1] = temp


# to print out the values
int_arr = [8,4,23,42,16,15]
insertion_sort(int_arr)

for i in range(len(int_arr)):
  print(int_arr[i])

  