def min_heap(fun=None):
    if fun is None:
        return Binomial(lambda a, b: 1 if a < b else -1 if a > b else 0)
    else:
        return Binomial(lambda a, b: 1 if fun(a) < fun(b) else -1 if fun(a) > fun(b) else 0)


class Binomial:
    def __init__(self, comparator):
        self._roots = []
        self._comparator = comparator

    def _singleton(self, val):
        heap = Binomial(self._comparator)
        heap._roots.append((val, []))
        return heap

    def size(self):
        return sum([2 ** i for i, root in self._roots if not root is None])

    def is_empty(self):
        return len(self._roots) == 0

    def _min(self):  # TODO optimize to O(1)
        minimum_root = None
        for idx, root in enumerate(self._roots):
            if root is None:
                continue
            if minimum_root is None or self._comparator(root[0], minimum_root[1]) == 1:
                minimum_root = (idx, root[0])
        return minimum_root

    def peek(self):
        return self._min()[1]

    def pop(self):
        if self.is_empty():
            return None

        idx, minimum = self._min()
        min_root, min_children = self._roots.pop(idx)
        child_heap = Binomial(self._comparator)
        child_heap._roots = min_children
        self.merge(child_heap)
        return min_root

    def insert(self, val):
        self.merge(self._singleton(val))

    def _safe_get_root(self, n, extending=False):
        if n >= len(self._roots):
            if extending:
                self._roots.extend([None] * (n - len(self._roots) + 1))
            else:
                return None
        return self._roots[n]

    def _trivial_merge_tree(self, i, other_subtree):
        my_subtree = self._roots[i]
        self._roots[i] = None
        if other_subtree is None:
            return i, my_subtree

        if self._comparator(my_subtree[0], other_subtree[0]) == -1:
            other_subtree[1].append(my_subtree)
            my_subtree = other_subtree
        else:
            my_subtree[1].append(other_subtree)
        return i+1, my_subtree

    def merge(self, other):
        i = 0
        while i < len(other._roots):
            if self._safe_get_root(i, True) is None:
                self._roots[i] = other._safe_get_root(i)
            else:
                new_pos, merged_subtree = self._trivial_merge_tree(i, other._safe_get_root(i))
                while not self._safe_get_root(new_pos, True) is None:
                    new_pos, merged_subtree = self._trivial_merge_tree(new_pos, merged_subtree)
                self._roots[new_pos] = merged_subtree
            i += 1

if __name__ == '__main__':
    pass