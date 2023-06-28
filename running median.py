def insertionsort(list, size):
    for i in range(1, size):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list


def median(list, size):
    if size % 2 != 0:
        median = list[int(((size+1)/2)-1)]
    else:
        median = (list[int((size/2)-1)]+list[int(size / 2)])/2
    return median


list = [2, 1, 5, 7, 2, 0, 5, 5]
size = len(list)
print(list)
list = insertionsort(list, size)
print(list)
print(f"median of the list is {median(list,size)}")
