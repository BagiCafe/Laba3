def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0:
        return 1

    rez = 1
    for i in range(1, n + 1):
        rez *= i
    return rez


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fib(n: int) -> int:
    if n < 0:
        raise ValueError("Число Фибоначчи определено только для неотрицательных n")
    if n == 0:
        return 0
    if n == 1:
        return 1

    n1, n2 = 0, 1
    for i in range(2, n + 1):
        n1, n2 = n2, n1 + n2
    return n2


def fib_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Число Фибоначчи определено только для неотрицательных n")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)