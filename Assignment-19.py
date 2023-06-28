class Array:

    def getArray(self, arr1, arr2, size):

        self.arr1 = arr1

        self.arr2 = arr2

        self.size = size
        print("Enter the array 1 elements")
        for i in range(self.size):
            col = []
            for j in range(self.size):
                col.append(int(input(f"element {i} {j}  ")))
            self.arr1.append(col)
        print("Enter the array 2 elements")
        for i in range(self.size):
            col = []
            for j in range(self.size):
                col.append(int(input(f"element {i} {j}  ")))
            self.arr2.append(col)

    def addArray(self, arr1, arr2, sum, size):

        self.arr1 = arr1

        self.arr2 = arr2

        self.size = size

        self.sum = sum
        for i in range(self.size):
            col = []
            for j in range(self.size):
                col.append(self.arr1[i][j]+self.arr2[i][j])
            self.sum.append(col)

    def displayArray(self, arr1, arr2, sum):

        self.arr1 = arr1

        self.arr2 = arr2

        self.sum = sum
        print("Array 1")

        print(arr1)

        print("Array 2")

        print(arr2)
        print("Sum")

        print(sum)


if __name__ == '__main__':
    arr1 = []
    arr2 = []
    sum = []
    size = int(input("Enter the size of array "))
    obj = Array()
    obj.getArray(arr1, arr2, size)
    obj.addArray(arr1, arr2, sum, size)
    obj.displayArray(arr1, arr2, sum)
