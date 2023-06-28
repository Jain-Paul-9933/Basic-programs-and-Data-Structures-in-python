arr1 = []
arr2 = []
arr3 = []
rows = int(input("Enter the row size "))
cols = int(input("Enter the column size "))
print("Enter the array 1 elements")
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(int(input(f"element {i} {j}  ")))
    arr1.append(col)
print("Enter the array 1 elements")
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(int(input(f"element {i} {j}  ")))
    arr2.append(col)
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(arr1[i][j]+arr2[i][j])
    arr3.append(col)
print(arr1)
print(arr2)
print(arr3)
