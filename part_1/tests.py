from part_1.samples.karatsuba import karatsuba
from part_1.samples.merge_sort import merge_sort
from part_1.samples.counting_inversion import brute_force_searching, sort_count_inv
from part_1.samples.quick_sorting import quick_sort, quicksort


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


def test_brute_force_searching():
    assert brute_force_searching([6, 5, 4, 3, 2, 1]) == 15
    assert brute_force_searching([0]) == 0
    assert brute_force_searching([1, 3, 4, 5, 2, 6]) == 3
    assert brute_force_searching([1, 0]) == 1
    assert brute_force_searching([1, 2, 5, 7, 5]) == 1


def test_sort_count_inversions():
    assert sort_count_inv([6, 5, 4, 3]) == ([3, 4, 5, 6], 6)
    assert sort_count_inv([0, 1, 3, 2]) == ([0, 1, 2, 3], 1)
    assert sort_count_inv([13, 4, 23, 43, 21, 1, 9, 56]) == ([1, 4, 9, 13, 21, 23, 43, 56], 12)
    assert sort_count_inv([13, 4, 23, 43, 21, 1, 9]) == ([1, 4, 9, 13, 21, 23, 43], 12)
    assert sort_count_inv([1]) == ([1], 0)
    assert sort_count_inv([1, 3, 4, 10, 10, 4, 3, 1]) == ([1, 1, 3, 3, 4, 4, 10, 10], 12)
    assert sort_count_inv([6, 5, 4, 3, 2, 1]) == ([1, 2, 3, 4, 5, 6], 15)


def test_quick_sort():
    assert quick_sort([]) == []
    assert quick_sort([2]) == [2]
    assert quick_sort([5, 6, 9]) == [5, 6, 9]
    assert quick_sort([2, 1, 0]) == [0, 1, 2]
    assert quick_sort([2, 1, 4, 3, 7, 5, 6, 9]) == [1, 2, 3, 4, 5, 6, 7, 9]