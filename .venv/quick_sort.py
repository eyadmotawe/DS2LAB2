from sort_strategy import *
from random import *

class QuickSort(sort_strategy):
    def partition(self, arr, low, high):
        random = low + randint(0,100000) % (high - low + 1)
        arr[random], arr[high] = arr[high], arr[random]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    def sort(self, arr, low, high):
        if low >= high:
            return arr
        pivot = self.partition(arr, low, high)
        self.sort(arr, low, pivot - 1)
        self.sort(arr, pivot + 1, high)
        return arr
