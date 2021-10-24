"""Module realize binary search
    quick sort and recursive factorial counting """
import random

def binary_search(array: list, item: "the item that should be found"):

    """
    Function implements binary search algorithm
    :argument array
        sorted list
    :argument item
        item that tries to found in list
    :return index: int
        index of item in array
    :return -1
        if item not found
    """

    length = len(array)
    left = 0
    right = length - 1
    middle = (left + right) // 2
    index = 0
    while left <= right:
        if array[middle] == item:
            return middle
        elif item < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle = (left + right) // 2
    return -1


def quick_sort(array: list) -> list:
    """
    Function sorts array in ascending order
    :return list
        sorted list
    """

    def partition(start, end):
        """Nested function that returns index of barrier element"""
        p_index = start
        barrier = array[end]
        i = start
        while i < end:
            if array[i] < barrier:
                array[p_index], array[i] = array[i], array[p_index]
                p_index += 1
            i += 1
        array[p_index], array[end] = array[end], array[p_index]
        return p_index

    stack = list()
    stack.append((0, len(array)-1))

    while stack:
        left, right = stack.pop()
        new_barrier = partition(left, right)

        if new_barrier - 1 > left:
            stack.append((left, new_barrier - 1))

        if new_barrier + 1 < right:
            stack.append((new_barrier + 1, right))

    return array


def fact(n: int):
    """Recursive factorial implementation"""
    if n < 0:
        raise TypeError("Only natural numbers allowed")
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n



