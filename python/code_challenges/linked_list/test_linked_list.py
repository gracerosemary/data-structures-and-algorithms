import unittest
from linked_list import LinkedList

def test_import():
    assert LinkedList

def test_empty_list():
    actual = LinkedList().head
    expected = None
    assert actual == expected

def test_insert():
    ll = LinkedList()
    ll.insert(5)
    actual = ll.head.value
    expected = 5
    assert actual == expected

def test_head_pointer():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.head.value
    expected = 3
    assert actual == expected

def test_insert_multiple():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.head.value, ll.head.next.value, ll.head.next.next.value
    expected = (3,2,1)
    assert actual == expected

def test_includes_true():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(1)
    expected = True
    assert actual == expected

def test_includes_false():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(100)
    expected = False
    assert actual == expected

def test_str_collection():
    ll = LinkedList()
    ll.insert('c')
    ll.insert('b')
    ll.insert('a')
    actual = str(ll)
    expected = "{a}->{b}->{c}->NULL"
    assert actual == expected
