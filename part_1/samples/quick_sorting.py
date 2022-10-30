from random import randint
from typing import List
from datetime import datetime
import os
import psutil


def swapper(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def partitioning(a: List[int], left, right) -> int:
    pivot = a[left]
    i = left + 1

    for j in range(i, right + 1):
        if array[j] < pivot:
            swapper(a, i, j)
            i += 1

    swapper(a, left, i - 1)
    return i - 1


# In place Quick Sort
def quick_sort(a: List[int], l: int = 0, r: int = None):
    if r is None:
        r = len(a) - 1

    if l >= r:
        return a

    # pivot = randint(start, end)
    # swapper(array, len(array)//2, start)

    pivot_index = partitioning(a, l, r)

    quick_sort(a, l, pivot_index - 1)
    quick_sort(a, pivot_index + 1, l)

    return a


# Real Python Example requires additional memory
def quicksort(a: List[int]) -> List[int]:
    low, same, high = [], [], []
    if len(a) <= 1:
        return a

    # pivot = array[randint(0, len(array)-1)]
    pivot = array[len(a) // 2]

    for item in a:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


array = [randint(0, 1000) for i in range(1000)]
sorted_version = sorted(array)
arr = [9, 3, 5, 2, 8, 7, 1, 0, 21, 14, 12, 17, 15]
start = datetime.now()
arr_1 = quicksort(array)
finish_1 = datetime.now() - start
process_1 = psutil.Process(os.getpid())
arr_1_mem = process_1.memory_info()[0] / float(2 ** 20)

start = datetime.now()
arr_2 = quick_sort(array)
finish_2 = datetime.now() - start
process_2 = psutil.Process(os.getpid())
arr_2_mem = process_2.memory_info()[0] / float(2 ** 20)

start = datetime.now()
arr_3 = sorted(array)
finish_3 = datetime.now() - start
process_3 = psutil.Process(os.getpid())
arr_3_mem = process_3.memory_info()[0] / float(2 ** 20)

print(
    f"quicksort => time: {finish_1.microseconds}, memory: {arr_1_mem}, test: {'success' if arr_1 == sorted_version else 'fail'}")
print(
    f"quick_sort => time: {finish_2.microseconds}, memory: {arr_2_mem}, test: {'success' if arr_2 == sorted_version else 'fail'}")
print(
    f"built_in sort => time: {finish_3.microseconds}, memory: {arr_3_mem}, test: {'success' if arr_3 == sorted_version else 'fail'}")
