"""
Module with tests for to_test module
uses pytests library
"""
import datetime

import pytest
import to_test as t


def test_pos_even_odd():
    """Positive case even_odd()"""
    assert t.even_odd(10) == "even", "Should be even"
    assert t.even_odd(5) == "odd", "Should be odd"
    assert isinstance(t.even_odd(3), str), "Should be string"


def test_neg_even_odd():
    """Negative case even_odd()"""
    with pytest.raises(TypeError) as error:
        t.even_odd("a")
        assert isinstance(error, TypeError), "TypeError must be raises"

    assert t.even_odd(12345) != "even", "Should be odd"
    assert t.even_odd(12346) != "odd", "Should be even"


@pytest.mark.parametrize("nums, expected", [
    ((1, 2, 3), 6),
    ((4.002, 5.1, 6), 15.102),
    ([-1, -2, -3], -6),
    ((0, 0, 0, 0, 0), 0)
])
def test_pos_sum_all(nums, expected):
    """Positive cases for sum_all()"""

    assert t.sum_all(*nums) == expected, f"Should be {expected} "


def test_neg_sum_all():
    """Negative cases for sum_all()"""
    with pytest.raises(TypeError) as error:
        t.sum_all("asd")
        assert isinstance(error, TypeError)

    assert t.sum_all(100, 100, 100) != -300, "Should be 300"


def test_pos_time_of_day():
    """Positive cases for time_of_day()"""
    now = datetime.datetime.now()
    res = ""
    time_of_day = ("night", "morning", "afternoon", "night" )
    if 0 <= now.hour < 6:
        res = time_of_day[0]
    elif 6 <= now.hour < 12:
        res = time_of_day[1]
    elif 12 <= now.hour < 18:
        res = time_of_day[2]
    else:
        res = time_of_day[3]

    assert t.time_of_day() == res, f"Should be {res}"



def test_neg_time_of_day():
    """Positive cases for time_of_day()"""
    assert t.time_of_day() is not None, "Should be str"
    assert not isinstance(t.time_of_day(), int), "Should be str"


@pytest.fixture
def new_product():
    """Creates object of Product class with price 20.5"""
    return t.Product("Water", 20.5)


def test_pos_product_init(new_product):
    """Positive cases for Product.__init()__"""

    assert isinstance(new_product.title, str), "Should be str"
    assert isinstance(new_product.price, float), "Should be float"
    assert isinstance(new_product.quantity, int), "Should be int"
    assert new_product.title == "Water", "Should be Water"
    assert new_product.price == 20.5, "Should be 20.5"
    assert new_product.quantity == 1, "Should be 1"


def test_neg_product_init():
    """Negative cases for Product.__init()"""
    assert new_product.title != "water", "Should be Water"
    assert new_product.price != 21.5, "Should be 20.5"
    assert new_product.quantity != 0, "Should be 1"


















