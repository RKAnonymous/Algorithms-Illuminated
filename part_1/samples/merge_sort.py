from typing import List


def merge(first_half: List[int], second_half: List[int]) -> List[int]:
    i, j, result = 0, 0, list()
    while len(result) < len(first_half) + len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1

        if i == len(first_half):
            result += second_half[j:]
            break

        if j == len(second_half):
            result += first_half[i:]
            break

    return result


def merge_sort(arr: List[int]) -> List[int]:
    length = len(arr)

    if length < 2:
        return arr

    first_half = merge_sort(arr[:length//2])
    second_half = merge_sort(arr[length//2:])

    return merge(first_half, second_half)
