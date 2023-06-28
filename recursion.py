# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonacci(n-1)+fibonacci(n-2))


# n = 10
# if n <= 0:
#     print("Invalid Input")
# else:
#     print("Fibonacci series:")
# for i in range(n):
#     print(fibonacci(i))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


n = 10
print(f"Factorial of {n} is {factorial(n)} ")
