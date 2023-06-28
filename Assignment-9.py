size = int(input("Enter the size of the array "))
array_1 = []
array_2 = []
for i in range(size):
    array_1.append(int(input(f"enter element {i} ")))
array_2 = array_1.copy()
element = int(input("Enter the element to be inserted "))
array_2.append(element)
print(array_1)
print(array_2)
