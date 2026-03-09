from sort_strategy import *

class InsertionSort(sort_strategy):
    def sort(self, arr, low, high):
        n = high+1
        for i in range(1, n):
            key = arr[i]
            j = i
            while j > 0 and key < arr[j - 1]:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = key
        return arr