class Stack:
    def __init__(self):
        self.spisok = []

    def push(self, x: int) -> None:
        self.spisok.append(x)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError()
        return self.spisok.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError()
        return self.spisok[-1]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self.spisok)


class Queue:
    def __init__(self):
        self.spisok = []

    def enqueue(self, x: int) -> None:
        self.spisok.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError()
        return self.spisok.pop(0)

    def front(self) -> int:
        if self.is_empty():
            raise IndexError()
        return self.spisok[0]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self.spisok)