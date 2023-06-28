def add(a, b):

    print(f"Sum is {a+b} ")


def sub(a, b):

    print(f"diff is {a-b} ")


def mul(a, b):

    print(f"Product is {a*b}")


def div(a, b):

    print(f"quotient is {a/b}")


if __name__ == '__main__':

    print("1:Addition")
    print("2:Substraction")
    print("3:Multiplication")
    print("4:Division")
    choice = int(input("Enter the choice  "))
    a = int(input("Enter the first value "))
    b = int(input("Enter the second value "))
    print()
    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)
    else:
        print("Enter the valid choice")
