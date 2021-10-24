"""Test cases for algorithm.py"""

import pytest
import random
from data_structures_and_algorithms.algorithms.src import algorithms as alg


@pytest.mark.parametrize("array, find, expected", [
    ([x for x in range(100)], 50, 50),
    ([x for x in range(0, 121, 3)], 5, -1),
    ([0], 1, -1)

])
def test_binary_search(array, find, expected):
    """Test cases for binary_search() """
    assert alg.binary_search(array, find) == expected, f"Should be{expected}"


@pytest.mark.parametrize("array", [
    ([random.randint(1, 100) for x in range(100)]),
    ([random.randint(-200, 100) for x in range(100)]),
    ([random.randint(0, 1) for x in range(10000)]),
    ([100 for x in range(100)])

])
def test_quick_sort(array):
    """Test cases for quick_sort()"""
    assert alg.quick_sort(array) == sorted(array)


def test_fact():
    """Test cases for fact()"""
    assert alg.fact(10) == 3628800, "Should be 3628800"
    assert alg.fact(0) == 1, "Should be 1"
    with pytest.raises(TypeError) as error:
        alg.fact(-1)
        assert isinstance(error, TypeError)





