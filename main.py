from src import generators, fibo_factorial, all_sorting, Stack_Queue, benchmark


def main():

    print(" --- Демонстрация ГЕНЕРАЦИИ МАССИВА ---")
    random_array = generators.rand_int_array(8, 1, 20)
    unique_array = generators.rand_int_array(6, 1, 10, distinct=True)
    nearly_sorted = generators.nearly_sorted(8, 2)
    many_duplic = generators.many_duplicates(8, 3)
    reverse_array = generators.reverse_sorted(8)
    random_floats = generators.rand_float_array(5, 0.0, 1.0)

    print(f"Случайный: {random_array}")
    print(f"Уникальный: {unique_array}")
    print(f"Почти отсортированный: {nearly_sorted}")
    print(f"Много дубликатов: {many_duplic}")
    print(f"Обратный порядок: {reverse_array}")
    print(f"Дробные числа: {[f'{x:.2f}' for x in random_floats]}")


    print("\n --- Демонстрация ФИБОНАЧЧИ ---")
    for n in [0, 1, 7, 15]:
        rez_iter = fibo_factorial.fibo(n)
        rez_rec = fibo_factorial.fibo_recursive(n)
        print(f"fibo({n}): итеративный={rez_iter}, рекурсивный={rez_rec}")


    print("\n --- Демонстрация ФАКТОРИАЛ ---")
    for n in [0, 1 , 7, 15]:
        rez_iter = fibo_factorial.factorial(n)
        rez_rec = fibo_factorial.factorial_recursive(n)
        print(f"factorial({n}): итеративный={rez_iter}, рекурсивный={rez_rec}")


    print("\n --- Демонстрация ВСЕХ СОРТИРОВОК ---")
    test_int = [111, 28, 8, 0, 6, 3, 7, 4, 3, 1]
    test_float = [0.5, 0.3, 0.8, 0.1, 0.9, 0.3, 0.4]

    print(f"Исходный массив: {test_int}")
    print(f"Пузырьковая: {all_sorting.bubble_sort(test_int.copy())}")
    print(f"Быстрая: {all_sorting.quick_sort(test_int.copy())}")
    print(f"Подсчетом: {all_sorting.counting_sort(test_int.copy())}")
    print(f"Поразрядная: {all_sorting.radix_sort(test_int.copy())}")
    print(f"Карманная (float): {all_sorting.bucket_sort(test_float.copy())}")
    print(f"Кучей: {all_sorting.heap_sort(test_int.copy())}")


    print("\n --- Демонстрация СТЕКА ---")
    stack = Stack_Queue.Stack()
    spicok = [52, 75, 0, 3, 9]

    print(f"СТЕК: {spicok}")
    for n in spicok:
        stack.push(n)

    print(f"Минимальный элемент: {stack.min()}, Размер стека: {len(stack)}, Верхний элемент: {stack.peek()}")
    print(f"Извлеченный элемент: {stack.pop()}")
    print(f"Минимальный элемент после извлеченного элемента: {stack.min()}")
    print(f"Верхний элемент после извлеченного элемента: {stack.peek()}")


    print("\n --- Демонстрация ОЧЕРЕДИ ---")
    queue = Stack_Queue.Queue()
    spicok = [36, 856, 10, 1, 9, 77]

    print(f"ОЧЕРЕДЬ: {spicok}")
    for n in spicok:
        queue.enqueue(n)

    print(f"Первый элемент: {queue.front()}, Размер очереди: {len(queue)}")
    print(f"Извлеченный элемент: {queue.dequeue()}")
    print(f"Первый элемент после извлеченного элемента: {queue.front()}")


    print("\n --- Демонстрация БЕНЧМАРКОВ ---")
    arrays = {
        "100 элементов": generators.rand_int_array(100, 1, 1000),
        "500 элементов": generators.rand_int_array(500, 1, 1000),
        "Почти отсортированный": generators.nearly_sorted(50, 5),
        "Много дубликатов": generators.many_duplicates(500, 10)
    }

    algos = {
        "bubble_sort": all_sorting.bubble_sort,
        "quick_sort": all_sorting.quick_sort,
        "heap_sort": all_sorting.heap_sort,
        "counting_sort": all_sorting.counting_sort,
        "radix_sort": all_sorting.radix_sort,
        "bucket_sort": all_sorting.bucket_sort
    }

    rez = benchmark.benchmark_sorts(arrays, algos)

    print("\nВремя выполнения (секунды):")
    print("-" * 85)
    print(f"{'Алгоритм':<15} {'100 эл.':<11} {'500 эл.':<11} {'Почт. от':<11} {'Много дубликатов':<14}")
    print("-" * 85)

    for algo_name, times in rez.items():
        row = f"{algo_name:<15}"
        for name_algo in arrays.keys():
            time = times.get(name_algo, 0)
            if time < 0.001:
                formatted_time = f"{time * 1000:.2f} мс"
            else:
                formatted_time = f"{time:.4f} с"
            row += f" {formatted_time:<11}"
        print(row)

if __name__ == "__main__":
    main()