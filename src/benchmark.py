import time


# Измеряет время выполнения функции
def timer_once(func, *args, **kwargs) -> float:
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


# Сравнивает производительности алгоритмов сортировки
def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    rez = {}
    for name, func in algos.items():
        rez[name] = {}

        for name_ar, spicok_ar in arrays.items():
            test_ar = spicok_ar.copy()
            time = timer_once(func, test_ar)
            rez[name][name_ar] = time
    return rez