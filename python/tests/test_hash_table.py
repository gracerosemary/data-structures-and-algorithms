import pytest
from challenges.hashtable.hashtable import Hashtable

def test_create():
    hashtable = Hashtable()
    assert hashtable

def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary

def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')
    # assert actual >= 0 and actual < hashtable.size
    assert 0 <= actual < hashtable.size 

def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary 

def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary 

def test_add_key_val():
    hashtable = Hashtable()
    hashtable.add('addition', 676)
    assert hashtable.contains('addition') == True

def test_retrieve_val_from_key():
    hashtable = Hashtable()
    hashtable.add('addition', 676)
    assert hashtable.get('addition') == 676

def test_for_null_key():
    hashtable = Hashtable()
    hashtable.add('addition', 676)
    assert hashtable.contains('subtraction') == False

def test_collision_handles():
    hashtable = Hashtable()
    hashtable.add('addition', 676)
    hashtable.add('dadition', 66)
    assert hashtable._hash('addition') == hashtable._hash('dadition')

def test_retrieve_val_from_collision():
    hashtable = Hashtable()
    hashtable.add('addition', 676)
    hashtable.add('dadition', 66)
    assert hashtable.get('addition') == 676