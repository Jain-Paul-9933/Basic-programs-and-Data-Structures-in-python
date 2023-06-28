def binarysearch(list, target, left, right, mid):
    if left <= right:
        mid = (left+right)//2
        if list[mid] == target:
            print(f"Element found at position {mid+1}")
        elif list[mid] > target:
            binarysearch(list, target, left, mid-1, mid)
        else:
            binarysearch(list, target, mid+1, right, mid)
    else:
        print("element not found")


list = [25, 71, 68, 44, 97, 13, 87, 36, 105, 59]
list.sort()
print(list)
len = len(list)
target = int(input("Enter the value to be searched  "))
left = 0
right = len-1
mid = (left+right)//2
binarysearch(list, target, left, right, mid)
