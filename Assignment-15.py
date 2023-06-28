

def getArray(array):
    for i in range(10):
        array.append(int(input(f"Enter Element {i} ")))


def displayArray(array):

    print(array)


if __name__ == '__main__':
    array = []
    getArray(array)
    displayArray(array)
