import pytest
from challenges.left_join.left_join import left_join

def test_one_match():
    left_hm = {"fond":"enamored"}
    right_hm = {"fond":"averse"}
    actual = left_join(left_hm, right_hm)
    expected = [['fond', 'enamored', 'averse']]
    assert actual == expected 

def test_two_matches():
    left_hm = {"fond":"enamored", "wrath":"anger"}
    right_hm = {"fond":"averse","wrath":"delight"}
    actual = left_join(left_hm, right_hm)
    expected = [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight']]
    assert actual == expected 

def test_one_NULL():
    left_hm = {"fond":"enamored", "wrath":"anger"}
    right_hm = {"fond":"averse","frustration":"delight"}
    actual = left_join(left_hm, right_hm)
    expected = [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'Null']]
    assert actual == expected 

def test_two_NULL():
    left_hm = {"fond":"enamored", "wrath":"anger"}
    right_hm = {"like":"averse","frustration":"delight"}
    actual = left_join(left_hm, right_hm)
    expected = [['fond', 'enamored', 'Null'], ['wrath', 'anger', 'Null']]
    assert actual == expected 