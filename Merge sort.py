def merge_list(list, left, right):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
            k += 1
        else:
            list[k] = right[j]
            j += 1
            k += 1
    while i < len_left:
        list[k] = left[i]
        i += 1
        k += 1
    while j < len_right:
        list[k] = right[j]
        j += 1
        k += 1
    print(list)


def mergesort(list):
    if len(list) <= 1:
        return
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    mergesort(left)
    mergesort(right)
    merge_list(list, left, right)


list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
mergesort(list)
print(list)
