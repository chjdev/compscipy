from heaps.Binomial import min_heap as min_binomial_heap
from heaps.Binary import min_heap as min_binary_heap


def random(max_num=1000):
    mod = 1 << 20
    sub = mod >> 1
    t = 0
    for k in range(1, max_num + 1):
        t = (615949 * t + 797807) % mod
        yield t - sub


def test(heap, num):
    min_number = 2 ** 20
    for number in random(num):
        min_number = min(min_number, number)
        heap.insert(number)

    min_number_heap = heap.pop()
    assert min_number == min_number_heap

    print(min_number_heap)
    while min_number_heap is not None:
        new_min_number_heap = heap.pop()
        if new_min_number_heap is not None:
            assert min_number_heap < new_min_number_heap
        min_number_heap = new_min_number_heap
    print("done")


if __name__ == '__main__':
    test(min_binary_heap(), 1000)
    test(min_binomial_heap(), 1000)
