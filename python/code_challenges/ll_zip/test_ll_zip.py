from linked_list import LinkedList
from ll_zip import zipLists

def test_import():
    assert LinkedList

def test_same_length():
  list1 = LinkedList()
  list1.append_node(1)
  list1.append_node(3)
  list1.append_node(5)
  list2 = LinkedList()
  list2.append_node(2)
  list2.append_node(4)
  list2.append_node(6)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{2}->{3}->{4}->{5}->{6}->NULL"
  assert actual == expected

def test_diff_length():
  list1 = LinkedList()
  list1.append_node(1)
  list1.append_node(3)
  list1.append_node(5)
  list2 = LinkedList()
  list2.append_node(2)
  list2.append_node(4)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{2}->{3}->{4}->{5}->NULL"
  assert actual == expected

def test_opposite_diff_length():
  list1 = LinkedList()
  list1.append_node(1)
  list1.append_node(3)
  list2 = LinkedList()
  list2.append_node(2)
  list2.append_node(4)
  list1.append_node(5)
  actual = str(zipLists(list1, list2))
  expected = "{1}->{2}->{3}->{4}->{5}->NULL"
  assert actual == expected

def test_one_empty_list():
  list1 = LinkedList()
  list1.append_node(1)
  list1.append_node(2)
  list2 = LinkedList()
  actual = str(zipLists(list1, list2))
  expected = "{1}->{2}->NULL"
  assert actual == expected

