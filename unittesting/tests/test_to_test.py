"""
Module with tests for to_test module
uses pytests library
"""

import freezegun
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
        assert isinstance(error, TypeError), "Should be raise TypeError"

    assert t.sum_all(100, 100, 100) != -300, "Should be 300"


def test_pos_time_of_day():
    """Positive cases for time_of_day()"""
    with freezegun.freeze_time("2000-12-1 7:00:00"):
        assert t.time_of_day() == "morning"
    with freezegun.freeze_time("2000-12-1 3:00:00"):
        assert t.time_of_day() == "night"
    with freezegun.freeze_time("2000-12-1 13:00:00"):
        assert t.time_of_day() == "afternoon"
    with freezegun.freeze_time("2000-12-1 20:00:00"):
        assert t.time_of_day() == "night"


@pytest.fixture
def new_product_fixt():
    """Creates object of Product class with price 20.5"""
    return t.Product("Water", 20.5)


def test_pos_product_init(new_product_fixt):
    """Positive cases for Product.__init()__"""

    assert isinstance(new_product_fixt.title, str), "Should be str"
    assert isinstance(new_product_fixt.price, float), "Should be float"
    assert isinstance(new_product_fixt.quantity, int), "Should be int"
    assert new_product_fixt.title == "Water", "Should be Water"
    assert new_product_fixt.price == 20.5, "Should be 20.5"
    assert new_product_fixt.quantity == 1, "Should be 1"


def test_neg_product_init(new_product_fixt):
    """Negative cases for Product.__init()"""
    assert new_product_fixt.title != "water", "Should be Water"
    assert new_product_fixt.price != 21.5, "Should be 20.5"
    assert new_product_fixt.quantity != 0, "Should be 1"


@pytest.fixture
def product():
    """Creates Product with quantity = 10"""
    return t.Product("Bread", 18, 10)


def test_pos_subtract_quantity(product):
    """Positive cases for Product.subtract_quantity"""
    product.subtract_quantity()
    assert product.quantity == 9, "Should be 9"
    product.subtract_quantity(5)
    assert product.quantity == 4, "Should be 4"


def test_pos_add_quantity(product):
    """Positive cases for Product.add_quantity"""
    product.add_quantity()
    assert product.quantity == 11, "Should be 11"
    product.add_quantity(4)
    assert product.quantity == 15, "Should be 15"


def test_change_price(product):
    """Test case for price change"""
    product.change_price(15)
    assert product.price == 15, "Should be 15"
    temp = product.price
    product.change_price(10)
    assert product.price != temp, "Should be different from previous"


@pytest.fixture
def empty_shop():
    """Fixture returns empty shop"""
    return t.Shop()


def test_pos_shop_init_(empty_shop):
    """Test case for empty shop"""
    product_count = len(empty_shop.products)
    assert product_count == 0, "Should be zero"
    assert empty_shop.money == 0, "Should be zero"


@pytest.mark.parametrize("product, expected", [
    ("123", "123"),
    (123, 123),
    (50.5, 50.5),
    ({1: "a"}, {1: "a"})
])
def test_neg_shop_init_(product, expected):
    """Test cases for Shop __init__"""
    shop = t.Shop(product)
    assert shop.products == expected, f"Should be {expected}"


@pytest.fixture
def shop_with_product():
    """Fixture tHat returns Shop object with Product"""
    product = t.Product("Meat", 200.60, 100)
    return t.Shop(product)


def test_shop_init_full(shop_with_product):
    """Test case for Shop with one Product in constructor"""
    assert shop_with_product.products[0].title == "Meat"
    assert shop_with_product.products[0].quantity == 100
    assert shop_with_product.products[0].price == 200.60


@pytest.mark.parametrize("title, price, quantity", [
    ("Onion", 15, 100),
    ("Milk", 25.23, 87),
    ("Wine", 89, 50)
])
def test_pos_shop_add_product(shop_with_product, title, price, quantity):
    """Test case for Shop.add_product"""
    product = t.Product(title, price, quantity)
    shop_with_product.add_product(product)
    assert shop_with_product.products[1].title == title, f"Should be {title}"
    assert shop_with_product.products[1].price == price, f"Should be {price}"
    assert shop_with_product.products[1].quantity == quantity, f"Should be {quantity}"
    assert len(shop_with_product.products) == 2, f"Should be 2"


@pytest.mark.parametrize("product, expectation", [
    ("Onion", "Onion"),
    (25.23, 25.23),
    (50, 50)
])
def test_neg_shop_add_product(shop_with_product, product, expectation):
    """Test case for Shop.add_product with wrong input!"""
    shop_with_product.add_product(product)
    assert shop_with_product.products[1] == expectation, f"Should be {expectation}"
    assert len(shop_with_product.products) == 2, f"Should be 2"


@pytest.fixture
def shop_with_five_products(shop_with_product):
    """
    Fixture returns Shop object with five Product object
    """
    shop_with_product.add_product(t.Product("Onion", 15, 50))  # Meat, 200.60, 100 already included
    shop_with_product.add_product(t.Product("Milk", 22.54, 45))
    shop_with_product.add_product(t.Product("Bread", 22.41, 55))
    shop_with_product.add_product(t.Product("Beer", 67.25, 40))
    return shop_with_product


@pytest.mark.parametrize("title, index", [
    ("Onion", 1),
    ("Milk", 2),
    ("Beer", 4),
    ("Meat", 0),
    ("Water", None)
])
def test_pos__get_product_index(shop_with_five_products, title, index):
    """Test cases for Shop._get_product_index()"""
    assert shop_with_five_products._get_product_index(title) == index, f"Should be {index}"

@pytest.mark.parametrize("title, expected",[
    (123, None),
    (["Meat", "Onion"], None),
    (None, None),
    (print, None),
    ({1, 2, 3}, None),
    ({1: "a", 2: "3"}, None)
])
def test_neg__get_product_index(shop_with_five_products, title, expected):
    """Negative cases for Shop._get_product_index()"""
    assert shop_with_five_products._get_product_index(title) == expected, f"Should be {expected}"


@pytest.mark.parametrize("title, quantity, expected", [
    ("Meat", 1, 200.60),
    ("Onion", 10, 150),
    ("Fresh cream", 1, None)

])
def test_pos_sell_product(shop_with_five_products, title, quantity, expected):
    """Positive test cases for Shop.sell_product()"""
    assert shop_with_five_products.sell_product(title, quantity) == expected, \
        f"Should be {expected}"


def test_pos_sell_product_with_deletion(shop_with_five_products):
    """
    Test cases for Shop.sell_product() with removing product from shop
    Also tests Product.subtract_quantity()
    """
    shop_with_five_products.sell_product("Meat", 100)
    assert shop_with_five_products.products[0].title != "Meat"
    shop_with_five_products.sell_product("Onion", 10)
    assert shop_with_five_products.products[0].quantity == 40, "Should be 40"


def test_neg_sell_product(shop_with_five_products):
    """Test cases for Shop.sell_product() with raising error"""
    with pytest.raises(ValueError) as error:
        shop_with_five_products.sell_product("Onion", 100)
        assert isinstance(error, ValueError)

    with pytest.raises(TypeError) as error:
        shop_with_five_products.sell_product("Onion", None)
        assert isinstance(error, TypeError)
