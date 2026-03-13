from sort_strategy import *
from random import *

class QuickSort(sort_strategy):
    def partition(self, arr, low, high):
        random_index = low + randint(0, 100000) % (high - low + 1)
        arr[random_index], arr[low] = arr[low], arr[random_index]
        pivot = arr[low]
        lastS1 = low
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                lastS1 += 1
                arr[lastS1], arr[j] = arr[j], arr[lastS1]

        arr[low], arr[lastS1] = arr[lastS1], arr[low]
        return lastS1

    def sort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.sort(arr, low, pivot - 1)
            self.sort(arr, pivot + 1, high)
        return arr

