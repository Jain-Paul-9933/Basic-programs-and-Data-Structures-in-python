num = int(input("Enter the number for multiplication table  "))
for i in range(1, 11):
    res = i * num
    print(str(i) + " x " + str(num) + " = " + str(res))
    print("")
