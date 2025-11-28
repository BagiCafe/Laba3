import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.all_sorting import bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort, bucket_sort

class TestSorting:
    def test_bubble_sort(self):
        assert bubble_sort([3, 1, 2]) == [1, 2, 3]
        assert bubble_sort([]) == []
        assert bubble_sort([13]) == [13]

    def test_quick_sort(self):
        assert quick_sort([3, 1, 2]) == [1, 2, 3]
        assert quick_sort([]) == []
        assert quick_sort([0]) == [0]

    def test_heap_sort(self):
        assert heap_sort([3, 1, 2]) == [1, 2, 3]
        assert heap_sort([]) == []
        assert heap_sort([52]) == [52]

    def test_counting_sort(self):
        assert counting_sort([3, 1, 2]) == [1, 2, 3]
        assert counting_sort([]) == []
        assert counting_sort([99]) == [99]

    def test_radix_sort(self):
        assert radix_sort([55, 143, 8]) == [8, 55, 143]
        assert radix_sort([]) == []
        assert radix_sort([7]) == [7]

    def test_bucket_sort(self):
        assert bucket_sort([0.3, 0.1, 0.2]) == [0.1, 0.2, 0.3]
        assert bucket_sort([]) == []
        assert bucket_sort([0.5]) == [0.5]