from abc import abstractmethod
from abc import ABCMeta


class Heap(metaclass=ABCMeta):

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def insert(self, val):
        pass

    @abstractmethod
    def merge(self, other):
        pass

if __name__ == '__main__':
    pass
