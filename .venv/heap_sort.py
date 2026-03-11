def max_heapify(A, n, i):
    largest = i
    left_son = 2 * i + 1
    right_son = 2 * i + 2

    if left_son < n and A[left_son] > A[largest]:
        largest = left_son

    if right_son < n and A[right_son] > A[largest]:
        largest = right_son

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A):
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)


def heap_sort(A):
    n = len(A)

    build_max_heap(A)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)



