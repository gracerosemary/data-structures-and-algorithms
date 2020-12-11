import math

def insertShiftArray(newarray: list, n: int) -> list:
    """Returns error message if n is not an integer, else if the array length is even, it inserts n after the midpoint, else if the array length is odd, it inserts n after the midpoint + 1, and then returns the new array with the inserted integer.
    :param list of integers, n = integer
    :type: integers
    :rtype: list
    """
    midpoint = int(len(newarray) / 2) 
    rounded_midpoint = math.ceil(midpoint) + 1
    error_message = 'That\'s cheating! Please enter a valid integer.'

    if type(n) is not int:
        return error_message
    elif len(newarray) % 2 == 0:
        newarray.insert(midpoint, n)
        return newarray
    else:
        newarray.insert(rounded_midpoint, n)
        return newarray

    # Attribution for checking data type: https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python