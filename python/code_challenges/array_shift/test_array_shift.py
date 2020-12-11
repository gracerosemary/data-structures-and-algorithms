# kept getting a module not found error so i moved the test into the array_shift folder, as it seemed to work
# from tests folder, tried array_shift.array_shift and array_shift and both didn't work

import unittest
from array_shift import insertShiftArray

def test_small_number():
    actual = insertShiftArray([1,2], 1)
    expected = [1,1,2]
    assert actual == expected

def test_big_number():
    actual = insertShiftArray([1,2], 10000)
    expected = [1,10000,2]
    assert actual == expected

def test_empty_array():
    actual = insertShiftArray([], 1)
    expected = [1]
    assert actual == expected

def test_even_length_and_int():
    actual = insertShiftArray([1,2,4,5], 3)
    expected = [1,2,3,4,5]
    assert actual == expected

def test_odd_length_and_int():
    actual = insertShiftArray([1,2,3,5,6], 4)
    expected = [1,2,3,4,5,6]
    assert actual == expected

def test_string_text_failure():
    actual = insertShiftArray([1,3], 'two')
    expected = AssertionError
    assert actual == expected

def test_float_failure():
    actual = insertShiftArray([1,3], 2.0)
    expected = AssertionError
    assert actual == expected