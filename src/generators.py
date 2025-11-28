import random


# Генерация случайного массива целых чисел
def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    random.seed(seed)
    if distinct:
        if (hi - lo + 1) < n:
            raise ValueError(f"Невозможно сгенерировать {n} уникальных элементов в диапазоне [{lo}, {hi}]")
        return random.sample(range(lo, hi + 1), n)
    else:
        return random.choices(range(lo, hi + 1), k=n)


# Генерация почти отсортированного массива
def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    random.seed(seed)
    a = list(range(n))
    for i in range(swaps):
        j = random.randint(0, n - 1)
        k = random.randint(0, n - 1)
        a[j], a[k] = a[k], a[j]
    return a

# Генерация массива с большим количеством дубликатов
def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    random.seed(seed)
    spicok = list(range(k_unique))
    return [random.choice(spicok) for i in range(n)]


# Генерация обратного отсортированного массива
def reverse_sorted(n: int) -> list[int]:
    return [i for i in range(n - 1, -1, -1)]


# Генерация случайного массива дробных чисел
def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    random.seed(seed)
    return [random.uniform(lo, hi) for i in range(n)]