nums = [1, 2, 3, 1]
for i in range(len(nums)):
    j = 0
    flag = False
    while i != j:
        if nums[i] != nums[j]:
            flag = True
if flag == True:
    return False
