def heapify(list, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and list[i] < list[l]:
        largest = l
    if r < n and list[largest] < list[r]:
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)


def search(list, val):
    size = len(list)
    for i in range(size):
        if list[i] == val:
            print(f"{val} found at position {i}")
            print(
                f"parent of {val} is {list[(i-1)//2]} at position {(i-1)//2}")
            break


def insert(list, newNum):
    size = len(list)
    if size == 0:
        list.append(newNum)
    else:
        list.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(list, size, i)


def deletion(list, num):
    size = len(list)
    for i in range(0, size):
        if num == list[i]:
            break
    list[i], list[size-1] = list[size-1], list[i]
    list.pop(4)
    for i in range((size//2) - 1, -1, -1):
        heapify(list, len(list), i)


list = []
insert(list, 2)
insert(list, 3)
insert(list, 9)
insert(list, 5)
insert(list, 4)
insert(list, 8)
insert(list, 7)
print(list)
# deletion(list, 4)
search(list, 7)
