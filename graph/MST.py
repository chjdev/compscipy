from heaps.Binomial import min_heap
from .Graph import Graph


def undirected_prim(graph: Graph):
    queue = min_heap(lambda a: a[2]['weight'])
    node_count = 0
    node = 0
    used = set()
    used.add(node)
    while node_count < graph.size():
        edges = graph.edges(node)
        for outbound in [edge for edge in edges if not edge[1] in used]:
            queue.insert(outbound)
        edge = queue.pop()
        while edge is not None and edge[1] in used:
            edge = queue.pop()
        if edge is None:
            break
        yield edge
        node = edge[1]
        used.add(node)
        node_count += 1


def _dijkstra_weight_closure(graph):
    return lambda a: graph.meta(a).get('_reach')


def undirected_dijkstra(graph: Graph, from_node: int, to_node: int):
    used = set()
    used.add(from_node)
    node_queue = min_heap(_dijkstra_weight_closure(graph))
    graph.meta(from_node)['_reach'] = 0
    node_queue.insert(from_node)
    while not node_queue.is_empty():
        investigate = node_queue.pop()
        my_weight = graph.meta(investigate).get('_reach')
        edges = graph.edges(investigate)
        for a, b, meta in edges:
            new_weight = my_weight + meta['weight']
            current_weight = graph.meta(b).get('_reach')
            if current_weight is None or new_weight < current_weight:
                graph.meta(b)['_reach'] = new_weight
                graph.meta(b)['_from'] = a
            if b not in used:
                node_queue.insert(b)
            used.add(b)
    cursor = to_node
    yield cursor
    while cursor != from_node:
        cursor = graph.meta(cursor)['_from']
        yield cursor



if __name__ == '__main__':
    pass