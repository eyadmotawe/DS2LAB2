from sort_strategy import *

class BubbleSort(sort_strategy):
    def sort(self, arr, low, high):
        n = high+1
        for i in range(n - 1):
            is_sorted = True
            for j in range(n - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    is_sorted = False
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
            if is_sorted:
                return arr
        return arr