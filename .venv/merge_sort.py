from sort_strategy import *

class MergeSort(sort_strategy):
    def merge(self, left, right):
        if left is None or right is None:
            return
        n = len(left)
        m = len(right)
        i = j = 0
        result = []
        while i < n and j < m:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < n:
            result.append(left[i])
            i += 1
        while j < m:
            result.append(right[j])
            j += 1
        return result


    def sort(self, arr, left, right):
        left = 0
        right = len(arr)
        if len(arr) <= 1:
            return arr
        mid = (left + right) // 2
        left_half = self.sort(arr[left : mid], left, mid)
        right_half = self.sort(arr[mid : right], mid, right+1)
        return self.merge(left_half, right_half)

