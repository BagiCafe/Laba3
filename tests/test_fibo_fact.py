import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from src.fibo_factorial import factorial, factorial_recursive, fibo, fibo_recursive

class TestFactorial:
    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(7) == 5040

    def test_factorial_recursive(self):
        assert factorial_recursive(0) == 1
        assert factorial_recursive(1) == 1
        assert factorial_recursive(7) == 5040

    def test_factorial_error(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_recursive_error(self):
        with pytest.raises(ValueError):
            factorial_recursive(-7)

class TestFibo:
    def test_fibo(self):
        assert fibo(0) == 0
        assert fibo(1) == 1
        assert fibo(13) == 233

    def test_fibo_recursive(self):
        assert fibo_recursive(0) == 0
        assert fibo_recursive(1) == 1
        assert fibo_recursive(13) == 233

    def test_fibo_error(self):
        with pytest.raises(ValueError):
            fibo(-1)

    def test_fibo_recursive_error(self):
        with pytest.raises(ValueError):
            fibo_recursive(-13)