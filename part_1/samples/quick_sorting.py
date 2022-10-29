from typing import List, Union


def swapper(array, i, j):
    array[i], array[j] = array[j], array[i]


def partitioning(array: List[int], left, right) -> int:
    # pivot_index = randint(0, len(array) - 1)
    # assuming the pivot element index is 0

    pivot = array[left]
    i = left + 1

    for j in range(i, right + 1):
        if array[j] < pivot:
            swapper(array, i, j)
            i += 1

    swapper(array, left, i-1)
    return i - 1


# In place Quick Sort
def quick_sort(array: List[int], start: int = 0, end: int = None):
    if end is None:
        end = len(array) - 1

    if start >= end:
        return array

    pivot_index = partitioning(array, start, end)

    low = quick_sort(array, start, pivot_index - 1)
    high = quick_sort(array, pivot_index + 1, end)

    return array


# Real Python Example requires additional memory
def quicksort(array: List[int]) -> List[int]:
    low, same, high = [], [], []
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

from datetime import datetime

arr = [9, 3, 5, 2, 8, 7, 1, 0]
start = datetime.now()
arr_1 = quicksort(arr)
finish_1 = datetime.now() - start

start = datetime.now()
arr_2 = quick_sort(arr)
finish_2 = datetime.now() - start

start = datetime.now()
arr_3 = sorted(arr)
finish_3 = datetime.now() - start

print("quicksort: ", finish_1, arr_1 == [0, 1, 2, 3, 5, 7, 8, 9])
print("quick_sort: ", finish_2, arr_2 == [0, 1, 2, 3, 5, 7, 8, 9])
print("built_in sort: ", finish_3, arr_3 == [0, 1, 2, 3, 5, 7, 8, 9])
