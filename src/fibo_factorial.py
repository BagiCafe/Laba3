def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал поддерживает только n >= 0")
    if n == 0:
        return 1

    rez = 1
    for i in range(1, n + 1):
        rez *= i
    return rez


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал поддерживает только n >= 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("Фибоначчи поддерживает только n >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1

    n1, n2 = 0, 1
    for i in range(2, n + 1):
        n1, n2 = n2, n1 + n2
    return n2


def fibo_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Фибоначчи поддерживает только n >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)