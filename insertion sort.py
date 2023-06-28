def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


list = [11, 9, 29, 7, 2, 15, 28]
insertionsort(list)
print(list)
