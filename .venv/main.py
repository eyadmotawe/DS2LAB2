from time import *
import random
from random import (randint)
from copy import *

import sort_strategy
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from merge_sort import *
from quick_sort import *
from selection_sort import *
from heap_sort import *
from hybrid_sort import *


def generate_random_array(size):
    return [randint(0, 10000) for i in range(size)]


def sort_with_strategy(arr, strategy : sort_strategy):
    return strategy.sort(arr, 0, len(arr) - 1)


def main(arr):
    print("-------------------------------------------------------------------")
    print(f"Testing Array Size: {len(arr)}")


    temp = arr.copy()
    begin = time()
    sort_with_strategy(temp, BubbleSort())
    end = time()
    print(f"BubbleSort    take time = {(end - begin) * 1000:.4f} ms")

    temp = arr.copy()
    begin = time()
    sort_with_strategy(temp, InsertionSort())
    end = time()
    print(f"InsertionSort take time = {(end - begin) * 1000:.4f} ms")

    temp = arr.copy()
    begin = time()
    sort_with_strategy(temp, SelectionSort())
    end = time()
    print(f"SelectionSort take time = {(end - begin) * 1000:.4f} ms")

    temp = arr.copy()
    begin = time()
    sort_with_strategy(temp, MergeSort())
    end = time()
    print(f"MergeSort     take time = {(end - begin) * 1000:.4f} ms")

    temp = arr.copy()
    begin = time()
    sort_with_strategy(temp, QuickSort())
    end = time()
    print(f"QuickSort     take time = {(end - begin) * 1000:.4f} ms")

    temp = arr.copy()
    begin = time()
    heap_sort(temp)
    end = time()
    print(f"Heap_Sort       take time = {(end - begin) * 1000:.4f} ms")

    temp = arr.copy()
    begin = time()
    mergeSort(temp, 0, len(temp) - 1, 10)
    end = time()
    print(f"Hybrid_Sort     take time = {(end - begin) * 1000:.4f} ms")

    print("-------------------------------------------------------------------")


# -----------------------------#
temp_sizes = [1000, 5000, 10000, 15000, 20000, 25000, 30000]

for i in range(len(temp_sizes)):
    test_arr = generate_random_array(temp_sizes[i])
    main(test_arr)