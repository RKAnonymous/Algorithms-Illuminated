from part_1.samples.karatsuba import karatsuba
from part_1.samples.merge_sort import merge_sort


def test_karatsuba():
    assert karatsuba(1234, 5432) == 6703088
    assert karatsuba(123, 5432) == 668136
    # assert karatsuba(12345, 6789) == 83810205
    # assert karatsuba(12, 5432) == 65184
    # assert karatsuba(100, 14) == 1400
    # assert karatsuba(100, 2) == 200
    assert karatsuba(0, 0) == 0
    assert karatsuba(0, 1) == 0
    # assert karatsuba(0, 1000) == 0
    # assert karatsuba(10, 1000) == 10000


def test_merge_sort():
    assert merge_sort([5, 3, 4, 2, 1, 6, 8, 7]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sort([5, 3, 4, 2, 1, 6, 8]) == [1, 2, 3, 4, 5, 6, 8]
    assert merge_sort([5, 3, 6, 8, 7]) == [3, 5, 6, 7, 8]
    assert merge_sort([5, 3, 4, 2, 1, 6, 8, 7, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort([0]) == [0]
    assert merge_sort([0, 0]) == [0, 0]
    assert merge_sort([1, 0, 1]) == [0, 1, 1]
    assert merge_sort([1, 1, 1]) == [1, 1, 1]
    assert merge_sort([]) == []



