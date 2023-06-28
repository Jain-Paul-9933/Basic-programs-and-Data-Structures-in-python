array = []
size = int(input("Enter the size of the array "))
print("Enter the values of the array ")
for i in range(size):
    array.append(int(input(f"enter element {i} ")))
for i in range(size):
    min_pos = i
    for i in range(i):
        if array[min_pos] > array[i]:
            temp = array[min_pos]
            array[min_pos] = array[i]
            array[i] = temp
print("The Sorted array is: ")
print(array)
