import pytest
from fifo_animal_shelter import Node, Cat, Dog, AnimalShelter, InvalidOperationError
    
# @pytest.mark.skip
def test_enqueue_one():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    actual = shelter.front.value
    expected = "cat"
    assert actual == expected

# @pytest.mark.skip
def test_enqueue_mult():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    actual = shelter.front.next.next.value
    expected = "dog"
    assert actual == expected

# @pytest.mark.skip
def test_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    actual = shelter.dequeue()
    expected = "cat"
    assert actual == expected

# @pytest.mark.skip
def test_peek():
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    actual = shelter.peek()
    expected = "cat"
    assert actual == expected

# @pytest.mark.skip
def test_peek_when_empty():
    shelter = AnimalShelter()
    with pytest.raises(InvalidOperationError) as e:
        shelter.peek()

    assert str(e.value) == "Method not allowed on empty collection"

# @pytest.mark.skip
def test_is_empty():
    shelter = AnimalShelter()
    with pytest.raises(InvalidOperationError) as e:
        shelter.peek()

    assert str(e.value) == "Method not allowed on empty collection"
