import sort_strategy
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from merge_sort import *
from quick_sort import *
from selection_sort import SelectionSort
from find_kth_smallest_element import *

def sort(arr, strategy : sort_strategy):
    return strategy.sort(arr, 0, len(arr)-1)

arr = [9,8,7,6,553464,8798,32,3,4,3,2,1,0]
arr = sort(arr, MergeSort())
print(arr)

arr = [9,8,7,6,553464,8798,32,3,4,3,2,1,0]
arr = sort(arr, QuickSort())
print(arr)

arr = [9,8,7,6,553464,8798,32,3,4,3,2,1,0]
arr = sort(arr, BubbleSort())
print(arr)

arr = [9,8,7,6,553464,8798,32,3,4,3,2,1,0]
arr = sort(arr, SelectionSort())
print(arr)

arr = [9,8,7,6,553464,8798,32,3,4,3,2,1,0]
arr = sort(arr, InsertionSort())
print(arr)

arr = [9,8,7,6,553464,8798,32,3,4,3,2,1,0]
print(find_kth_smallest_element(arr,0,len(arr)-1,5))