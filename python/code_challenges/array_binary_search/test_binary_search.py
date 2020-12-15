import unittest
from array_binary_search import BinarySearch

def test_return_neg_one():
    actual = BinarySearch([1,2,3,4], 5)
    expected = -1
    assert actual == expected

def test_odd_length():
    actual = BinarySearch([1,2,3], 3)
    expected = 2
    assert actual == expected

def test_even_length():
    actual = BinarySearch([1,2,3,7,9,12], 9)
    expected = 4
    assert actual == expected

def test_key_low():
    actual = BinarySearch([1,2,3,7], 1)
    expected = 0
    assert actual == expected

def test_key_high():
    actual = BinarySearch([1,2,3,7], 7)
    expected = 3
    assert actual == expected