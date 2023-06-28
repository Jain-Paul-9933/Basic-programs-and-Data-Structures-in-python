n = 4
a = 7
b = 11
for i in range(n, 0, -1):
    for j in range(a, b):
        print(j, end=" ")
    print()
    a = a-(i-1)
    b = b-i
