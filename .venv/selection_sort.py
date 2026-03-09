from sort_strategy import *

class SelectionSort(sort_strategy):
    def sort(self, arr, low, high):
        n = high +1
        for i in range(n - 1):
            min_indx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_indx]:
                    min_indx = j
            arr[i], arr[min_indx] = arr[min_indx], arr[i]
        return arr
