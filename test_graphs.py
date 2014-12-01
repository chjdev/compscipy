from graph.Graph import Undirected
from graph.MST import undirected_prim, undirected_dijkstra


def weight(w):
    return {'weight': w}


def graph1():
    graph = Undirected(4)
    graph.add_edge(0, 1, weight(1))
    graph.add_edge(1, 2, weight(2))
    graph.add_edge(2, 3, weight(5))
    graph.add_edge(3, 0, weight(4))
    graph.add_edge(0, 2, weight(3))
    return graph


def graph2():
    graph = Undirected(6)
    graph.add_edge(0, 1, weight(2))
    graph.add_edge(0, 2, weight(3))
    graph.add_edge(1, 2, weight(6))
    graph.add_edge(1, 3, weight(5))
    graph.add_edge(1, 4, weight(3))
    graph.add_edge(2, 4, weight(2))
    graph.add_edge(3, 4, weight(1))
    graph.add_edge(3, 5, weight(2))
    graph.add_edge(4, 5, weight(4))
    return graph


def graph3():
    graph = Undirected(6)
    graph.add_edge(0, 1, weight(7))
    graph.add_edge(0, 2, weight(9))
    graph.add_edge(0, 5, weight(14))
    graph.add_edge(1, 2, weight(10))
    graph.add_edge(1, 3, weight(15))
    graph.add_edge(2, 3, weight(11))
    graph.add_edge(2, 5, weight(2))
    graph.add_edge(3, 4, weight(6))
    graph.add_edge(5, 4, weight(9))
    return graph


def test_prim():
    graph = graph1()
    edges = [tuple(sorted((edge[0], edge[1]))) for edge in undirected_prim(graph)]
    print(edges)
    assert (0, 1) in edges
    assert (1, 2) in edges
    assert (0, 3) in edges
    assert len(edges) == 3

    graph = graph2()
    edges = [tuple(sorted((edge[0], edge[1]))) for edge in undirected_prim(graph)]
    print(edges)
    assert (0, 1) in edges
    assert (0, 2) in edges
    assert (2, 4) in edges
    assert (3, 4) in edges
    assert (3, 5) in edges
    assert len(edges) == 5


def test3():
    graph = graph2()
    path = list(undirected_dijkstra(graph, 0, 5))
    print(path)
    assert path == [5, 3, 4, 1, 0]

    graph = graph3()
    path = list(undirected_dijkstra(graph, 0, 4))
    print(path)
    assert path == [4, 5, 2, 0]
    path = list(undirected_dijkstra(graph, 0, 3))
    print(path)
    assert path == [3, 2, 0]

if __name__ == '__main__':
    test_prim()
    test3()
