from typing import List


def swapper(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def partitioning(array: List[int], left, right) -> int:
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

    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, end)

    return array


# Real Python Example requires additional memory
def quicksort(a: List[int]) -> List[int]:
    low, same, high = [], [], []
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    for item in a:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

