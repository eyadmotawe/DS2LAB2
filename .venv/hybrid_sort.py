def selection_sort(arr, left, right):
    for i in range(left, right):
        min_indx = i
        for j in range(i + 1, right + 1):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]
    return arr


# -----------------------------#


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right, STOP):
    if left >= right:
        return

    if (right - left + 1 <= STOP):
        selection_sort(arr, left, right)
        return

    mid = (left + right) // 2

    mergeSort(arr, left, mid, STOP)
    mergeSort(arr, mid + 1, right, STOP)

    merge(arr, left, mid, right)















