from .Heap import Heap
from math import ceil


def min_heap(fun=None):
    if fun is None:
        return Binary(lambda a, b: 1 if a < b else -1 if a > b else 0)
    else:
        return Binary(lambda a, b: 1 if fun(a) < fun(b) else -1 if fun(a) > fun(b) else 0)


class Binary(Heap):
    def __init__(self, comparator=lambda a, b: 1 if a > b else -1 if a < b else 0):
        self.heap = []
        self.comparator = comparator

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.heap[0]

    def pop(self):
        if self.is_empty():
            return None

        head = self.heap.pop(0)
        if self.is_empty():
            return head

        self.heap.insert(0, self.heap.pop())
        cursor = 0
        while cursor < self.size():
            left = cursor * 2 + 1
            right = left + 1
            if left >= self.size():
                break
            swap_with = right if right < self.size() and self.comparator(self.heap[left], self.heap[right]) == -1 else left
            if self.comparator(self.heap[swap_with], self.heap[cursor]) == 1:
                self.heap[swap_with], self.heap[cursor] = self.heap[cursor], self.heap[swap_with]
                cursor = swap_with
            else:
                cursor = self.size()
        return head

    def insert(self, val):
        self.heap.append(val)
        cursor = self.size() - 1
        while cursor > 0:
            parent_id = ceil(cursor / 2) - 1
            if self.comparator(val, self.heap[parent_id]) == 1:
                self.heap[parent_id], self.heap[cursor] = val, self.heap[parent_id]
                cursor = parent_id
            else:
                cursor = 0

    def merge(self, other):
        pass

    def __str__(self):
        return str(self.heap)

if __name__ == '__main__':
    pass
