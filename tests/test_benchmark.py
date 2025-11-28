import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.benchmark import timer_once, benchmark_sorts
from src.all_sorting import bubble_sort

class TestBenchmark:
    def test_timer_once(self):
        def empty_func():
            pass

        time_taken = timer_once(empty_func)
        assert isinstance(time_taken, float)
        assert time_taken > 0

    def test_benchmark_sorts(self):
        arrays = {"test": [3, 1, 2]}
        algos = {"bubble": bubble_sort}

        rez = benchmark_sorts(arrays, algos)

        assert "bubble" in rez
        assert "test" in rez["bubble"]
        assert isinstance(rez["bubble"]["test"], float)