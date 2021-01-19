# Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

new_array = [1,2,3,4,5]

def reverseArray(new_array):
    return new_array[::-1]

print(reverseArray(new_array))