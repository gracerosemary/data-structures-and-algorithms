import pytest
from queue_with_stacks import PseudoQueue, Stack, Node, InvalidOperationError
    
# @pytest.mark.skip
def test_enqueue_one():
    q = PseudoQueue()
    q.enqueue(20)
    actual = str(q)
    expected = "->[20]"
    assert actual == expected

# @pytest.mark.skip
def test_enqueue_mult():
    q = PseudoQueue()
    q.enqueue(20)
    q.enqueue(15)
    q.enqueue(10)
    q.enqueue(5)
    actual = str(q)
    expected = "->[5]->[10]->[15]->[20]"
    assert actual == expected

# @pytest.mark.skip
def test_dequeue():
    q = PseudoQueue()
    q.enqueue(20)
    actual = q.dequeue()
    expected = 20
    assert actual == expected

# @pytest.mark.skip
def test_dequeue_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError) as e:
        q.dequeue()

    assert str(e.value) == "Method not allowed on empty collection"

# @pytest.mark.skip
def test_dequeue_when_full():
    q = PseudoQueue()
    q.enqueue(20)
    q.enqueue(15)
    q.enqueue(10)
    q.enqueue(5)
    actual = q.dequeue()
    expected = 20
    assert actual == expected

# @pytest.mark.skip
def test_peek():
    q = PseudoQueue()
    q.enqueue("apple")
    actual = q.restack.peek()
    expected = "apple"
    assert actual == expected

# @pytest.mark.skip
def test_peek_when_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError) as e:
        q.restack.peek()

    assert str(e.value) == "Method not allowed on empty collection"

# @pytest.mark.skip
def test_peek_post_dequeue():
    q = PseudoQueue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()

    actual = q.destack.peek()
    expected = "bananas"
    assert actual == expected

# @pytest.mark.skip
def test_is_empty():
    q = PseudoQueue()
    with pytest.raises(InvalidOperationError) as e:
        q.destack.peek()

    assert str(e.value) == "Method not allowed on empty collection"
