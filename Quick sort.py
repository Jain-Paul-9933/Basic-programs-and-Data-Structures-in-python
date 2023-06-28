def swap(arr, a, b):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(list, start, end):
    pivotindex = start
    pivot = list[pivotindex]
    while start < end:
        while start < len(list) and list[start] <= pivot:
            start += 1
        while list[end] > pivot:
            end -= 1
        if start < end:
            swap(list, start, end)
    swap(list, pivotindex, end)
    return end


def quicksort(list, start, end):
    if start < end:
        pi = partition(list, start, end)
        quicksort(list, start, pi-1)  # left side partition
        quicksort(list, pi+1, end)  # right side partition


list = [11, 9, 29, 7, 2, 15, 28]
quicksort(list, 0, len(list)-1)
print(list)
