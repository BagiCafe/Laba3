import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from src.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array

class TestGenerators:
    def test_rand_int_array(self):
        a = rand_int_array(5, 2, 10, seed=42)
        assert len(a) == 5
        assert all(2 <= x <= 10 for x in a)

    def test_nearly_sorted(self):
        a = nearly_sorted(5, swaps=2, seed=32)
        assert len(a) == 5
        assert set(a) == {0, 1, 2, 3, 4}

    def test_many_duplicates(self):
        a = many_duplicates(5, k_unique=2, seed=52)
        assert len(a) == 5
        assert all(x in [0, 1] for x in a)

    def test_reverse_sorted(self):
        a = reverse_sorted(4)
        assert a == [3, 2, 1, 0]

    def test_rand_float_array(self):
        a = rand_float_array(3, seed=2)
        assert len(a) == 3
        assert all(0.0 <= x <= 1.0 for x in a)

    def test_rand_int_array_error(self):
        with pytest.raises(ValueError):
            rand_int_array(10, 3, 5, distinct=True)