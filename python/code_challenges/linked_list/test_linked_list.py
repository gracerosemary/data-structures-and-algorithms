import unittest, pytest
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

def test_append_single_end():
    ll = LinkedList()
    ll.append_node(2)
    actual = str(ll)
    expected = "{2}->NULL"
    assert actual == expected

def test_append_mullitple_end():
    ll = LinkedList()
    ll.append_node(3)
    ll.append_node(4)
    ll.append_node(5)
    actual = str(ll)
    expected = "{3}->{4}->{5}->NULL"
    assert actual == expected

def test_insert_before_head():
    ll = LinkedList()
    ll.insert(1) 
    ll.insert(3) 
    ll.insert(4) 
    ll.insertBefore(1, 2)
    actual = str(ll)
    expected = "{4}->{3}->{2}->{1}->NULL"
    assert actual == expected

def test_insert_before_middle():
    ll = LinkedList()
    ll.insert(2) 
    ll.insert(3) 
    ll.insert(4) 
    ll.insert(6) 
    ll.insertBefore(4, 5)
    actual = str(ll)
    expected = "{6}->{5}->{4}->{3}->{2}->NULL"
    assert actual == expected

def test_insert_after_middle():
    ll = LinkedList()
    ll.insert(2) 
    ll.insert(3) 
    ll.insert(4) 
    ll.insert(6) 
    ll.insertAfter(6, 5)
    actual = str(ll)
    expected = "{6}->{5}->{4}->{3}->{2}->NULL"
    assert actual == expected

def test_insert_after_tail():
    ll = LinkedList()
    ll.insert(2) 
    ll.insert(3) 
    ll.insertAfter(2, 1)
    actual = str(ll)
    expected = "{3}->{2}->{1}->NULL"
    assert actual == expected

def test_kth_longer_length():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    with pytest.raises(IndexError):
        ll.kthFromEnd(3)

def test_kth_same_length():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    actual = ll.kthFromEnd(1)
    expected = 2
    assert actual == expected 

def test_kth_negative():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    with pytest.raises(ValueError):
        ll.kthFromEnd(-1) 

def test_kth_of_one():
    ll = LinkedList()
    ll.insert(1)
    actual = ll.kthFromEnd(0)
    expected = 1
    assert actual == expected 

def test_kth_happy_path():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2) 
    ll.insert(3) 
    ll.insert(4) 
    ll.insert(5) 
    actual = ll.kthFromEnd(3)
    expected = 4
    assert actual == expected 