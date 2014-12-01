from abc import abstractmethod
from abc import ABCMeta


class Graph(metaclass=ABCMeta):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def add_vertex(self, meta):
        pass

    @abstractmethod
    def add_edge(self, a, b, meta):
        pass

    @abstractmethod
    def edges(self, a):
        pass

    @abstractmethod
    def meta(self, a, b):
        pass


class Undirected(Graph):

    def __init__(self, populate=0):
        self._vertices = []
        self._edges = {}
        if populate > 0:
            self.populate(populate)

    def size(self):
        return len(self._vertices)

    def populate(self, num_vertices):
        self._vertices = [{} for _ in range(0, num_vertices)]

    def add_vertex(self, meta={}):
        self._vertices.append(meta)
        return len(self._vertices) - 1

    def add_edge(self, a, b, meta={}):
        if a not in self._edges:
            self._edges[a] = {}
        if b not in self._edges:
            self._edges[b] = {}
        self._edges[a][b] = meta
        self._edges[b][a] = meta
        return a, b

    def edges(self, a):
        if not a in self._edges:
            return

        for b in self._edges[a]:
            yield a, b, self._edges[a][b]

    def meta(self, a, b=None):
        if b is None:
            return self._vertices[a]
        else:
            return self._edges[a, b]

if __name__ == '__main__':
    pass