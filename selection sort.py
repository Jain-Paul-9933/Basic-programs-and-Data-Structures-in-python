def selection_sort(list, size):
    for i in range(size-1):
        min_pos = i
        for j in range(i+1, size):
            if list[min_pos] > list[j]:
                min_pos = j
        temp = list[i]
        list[i] = list[min_pos]
        list[min_pos] = temp
    return list


list = [-2, 45, 0, 11, -9]
size = len(list)
print(selection_sort(list, size))
