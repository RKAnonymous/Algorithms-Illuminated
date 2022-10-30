from typing import List
from random import randrange


def swapper(a, i, j):
    a[i], a[j] = a[j], a[i]


def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1

    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            swapper(arr, j, i)

    swapper(arr, i + 1, r)
    return i + 1


def r_partition(arr, l, r):
    # print(l, r)
    # print(r-l+1)
    randomidx = randrange(r - l) + l
    print("random pivot: ", randomidx)
    swapper(arr, randomidx, r)
    return partition(arr, l, r)


def r_select(array: List[int], ith: int, start=0, end=None) -> int:
    # print(array)
    if start == end:
        return array[start]

    if end is None:
        end = len(array) - 1

    pivot_idx = r_partition(array, start, end)
    k = pivot_idx - start + 1

    if ith == k:
        return array[k]
    elif ith < k:
        return r_select(array, ith, start, pivot_idx - 1)
    else:
        return r_select(array, ith, pivot_idx + 1, end)


def Partition(a, pivot_index=0):
    i = 0
    if pivot_index != 0: a[0], a[pivot_index] = a[pivot_index], a[0]
    for j in range(len(a) - 1):
        if a[j + 1] < a[0]:
            a[j + 1], a[i + 1] = a[i + 1], a[j + 1]
            i += 1
    a[0], a[i] = a[i], a[0]
    return a, i


def RSelect(a, k):
    if len(a) == 1:
        return a[0]
    else:
        xpart = Partition(a, randrange(len(a)))
        a = xpart[0]  # partitioned array
        j = xpart[1]  # pivot index
        if j == k:
            return a[j]
        elif j > k:
            return RSelect(a[:j], k)
        else:
            k = k - j - 1
            return RSelect(a[(j + 1):], k)


x = [3, 1, 8, 4, 7, 9]  # [1, 3, 4, 7, 8, 9]
print(r_select(x, ith=0))
# for i in range(len(x)):
#     print("index: ", i)
#     print(f"Mine: {r_select(x, i)}")
#     print(f"example: {RSelect(x, i)}")
