# Пузырьковая сортировка
def bubble_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


# Быстрая сортировка
def quick_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    l = len(a) // 2
    mid = a[l]
    left = [x for x in a if x < mid]
    middle = [x for x in a if x == mid]
    right = [x for x in a if x > mid]
    return quick_sort(left) + middle + quick_sort(right)


# Сортировка подсчётом количества вхождений
def counting_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    maxim = max(a)
    minim = min(a)
    count = [0] * (maxim - minim + 1)
    for num in a:
        count[num - minim] += 1
    rez = []
    for num in range(len(count)):
        for i in range(count[num]):
            rez.append(num)
    return rez


# Поразрядная сортировка
def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return []
    maxim = max(a)
    discharge = 1
    while maxim // discharge > 0:
        buckets = [[] for i in range(base)]
        for num in a:
            digit = (num // discharge) % base
            buckets[digit].append(num)
        a = []
        for bucket in buckets:
            for n in bucket:
                a.append(n)
        discharge *= base
    return a


# Блочная сортировка
def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return []
    if buckets is None:
        buckets = len(a)
    bucket_list = [[] for i in range(buckets)]
    for num in a:
        index = int(num * buckets)
        if index >= buckets:
            index = buckets - 1
        bucket_list[index].append(num)

    rez = []
    for bucket in bucket_list:
        if bucket:
            sorted_bucket = bubble_sort_float(bucket)
            for n in sorted_bucket:
                rez.append(n)
    return rez

# Пузырьковая сортировка для float
def bubble_sort_float(a: list[float]) -> list[float]:
    if not a:
        return []
    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


# Пирамидальная сортировка
def heapify(a: list[int], n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def heap_sort(a: list[int]) -> list[int]:
    if not a:
        return []
    l = len(a)
    for i in range((l // 2) - 1, -1, -1):
        heapify(a, l, i)
    for i in range(l - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
    return a
