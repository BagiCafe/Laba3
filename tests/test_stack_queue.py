import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from src.Stack_Queue import Stack, Queue

class TestStack:
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_peek(self):
        stack = Stack()
        stack.push(25)
        assert stack.peek() == 25
        assert not stack.is_empty()

    def test_empty_stack(self):
        stack = Stack()
        assert stack.is_empty()

    def test_pop_error(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    def test_peek_error(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.peek()

    def test_min(self):
        stack = Stack()
        stack.push(1111)
        assert stack.min() == 1111

        stack.push(77)
        assert stack.min() == 77

        stack.push(80)
        assert stack.min() == 77

        stack.push(2)
        assert stack.min() == 2

        stack.push(4)
        assert stack.min() == 2

    def test_min_error(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.min()

class TestQueue:
    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(99)
        queue.enqueue(4)
        queue.enqueue(77)

        assert queue.dequeue() == 99
        assert queue.dequeue() == 4
        assert queue.dequeue() == 77
        assert queue.is_empty()

    def test_front(self):
        queue = Queue()
        queue.enqueue(36)
        assert queue.front() == 36
        assert not queue.is_empty()

    def test_empty_queue(self):
        queue = Queue()
        assert queue.is_empty()

    def test_dequeue_empty_error(self):
        queue = Queue()
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_front_empty_error(self):
        queue = Queue()
        with pytest.raises(IndexError):
            queue.front()