"""Week 11"""
def fibonacci(num):
    """FibonacciRecursionV1"""
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(int(input())))
