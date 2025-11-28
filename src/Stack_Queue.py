class Stack:
    def __init__(self):
        self.spicok = []
        self.min_spicok = []

    def push(self, x: int) -> None:
        self.spicok.append(x)
        if len(self.min_spicok) == 0 or x <= self.min_spicok[-1]:
            self.min_spicok.append(x)
        else:
            self.min_spicok.append(self.min_spicok[-1])

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Стек пустой")
        self.min_spicok.pop()
        return self.spicok.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.spicok[-1]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self.spicok)

    def min(self) -> int:
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self.min_spicok[-1]


class Queue:
    def __init__(self):
        self.spicok = []

    def enqueue(self, x: int) -> None:
        self.spicok.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Очередь пустая")
        return self.spicok.pop(0)

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("Очередь пустая")
        return self.spicok[0]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return len(self.spicok)