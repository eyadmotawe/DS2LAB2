from random import *

def find_kth_smallest_element(arr, low,high, k):
    if low > high:
        return None

    random = (low + randint(0, 100000)) % (high - low + 1)
    arr[random], arr[high] = arr[high], arr[random]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if i+1 == k:
        return arr[i+1]
    elif i+1 > k:
        return find_kth_smallest_element(arr, low, i, k)
    else:
        return find_kth_smallest_element(arr, i+2, high, k)
