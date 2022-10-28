from typing import List, Tuple


def brute_force_searching(array: List[int]) -> int:
    inversions = 0
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                inversions += 1

    return inversions


def merge_count_inv(first_half: List[int], second_half: List[int]) -> Tuple[List[int], int]:
    i = j = 0
    inversions = 0
    result = list()

    while len(result) < len(first_half) + len(second_half):
        if first_half[i] <= second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            inversions += len(first_half) - i
            j += 1

        if i == len(first_half):
            result += second_half[j:]
            break

        if j == len(second_half):
            result += first_half[i:]
            break

    return result, inversions


def sort_count_inv(array: List[int]) -> Tuple[List[int], int]:
    n = len(array)

    if n < 2:
        return array, 0
    else:
        left_half, left_inv = sort_count_inv(array[:n//2])
        right_half, right_inv = sort_count_inv(array[n//2:])

        result, split_inv = merge_count_inv(left_half, right_half)

        return result, int(left_inv + right_inv + split_inv)


print(sort_count_inv([6, 5, 4]))
# print(merge_count_inv([6], [3]))
