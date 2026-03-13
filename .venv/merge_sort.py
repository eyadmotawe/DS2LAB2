from sort_strategy import *

class MergeSort(sort_strategy):
    def merge(self, arr, first, mid, last):
        left = arr[first:mid+1]
        right = arr[mid+1:last+1]
        i = j = 0
        l = len(left)
        r = len(right)
        k = first

        while i < l and j < r:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < l:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < r:
            arr[k] = right[j]
            j += 1
            k += 1

    def sort(self, arr, first, last):
        if first < last:
            mid = (first + last) // 2
            self.sort(arr, first, mid)
            self.sort(arr, mid + 1, last)
            self.merge(arr, first, mid, last)
        return arr


