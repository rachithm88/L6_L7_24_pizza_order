"""Lab 6, part 1: execute every statement of pizza_order.py."""

import pytest
from pizza_order import pizza_price, order_discount, delivery_status


def test_large_pizza_with_five_toppings_and_cheese_burst():
    assert pizza_price("large", 5, True) == 780


def test_small_cheese_burst_is_rejected():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)


def test_unknown_size_is_rejected():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra-large", 0, True)


def test_negative_topping_count_is_rejected():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, True)


def test_order_below_minimum_has_no_discount():
    assert order_discount(299, "tuesday", True) == 0


def test_tuesday_student_discount():
    assert order_discount(600, "tuesday", True) == 350


def test_weekend_student_discount():
    assert order_discount(500, "saturday", True) == 50


def test_regular_weekday_student_discount():
    assert order_discount(500, "wednesday", True) == 100


def test_delivery_outside_service_area():
    assert delivery_status(15, 11) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(30, 3) == "on time"


def test_delivery_late():
    assert delivery_status(45, 3) == "late"


def test_delivery_after_forty_five_minutes():
    assert delivery_status(46, 3) == "free pizza"
