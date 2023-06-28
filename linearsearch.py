List = [1, 2, 8, 8, 3, 4, 6, 8, 4, 2]
target = int(input("Enter the element to be searched "))
for i in range(len(List)):
    if List[i] == target:
        print(f"Element found at position {i+1}")
