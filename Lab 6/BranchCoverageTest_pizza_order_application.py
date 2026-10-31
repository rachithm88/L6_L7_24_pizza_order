"""Lab 6, part 2: exercise true/false branches and boundary cases."""

import pytest
from pizza_order import pizza_price, order_discount, delivery_status


def test_plain_small_pizza():
    assert pizza_price("small", 0, False) == 200


def test_three_toppings_use_standard_rate():
    assert pizza_price("medium", 3, False) == 470


def test_four_toppings_use_reduced_extra_rate():
    assert pizza_price("large", 4, False) == 650


def test_cheese_burst_adds_one_hundred():
    assert pizza_price("medium", 2, True) == 530


def test_unknown_size_raises_value_error():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra-large", 0, False)


def test_negative_toppings_raise_value_error():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_small_cheese_burst_raises_value_error():
    with pytest.raises(ValueError, match="cheese burst not available for small"):
        pizza_price("small", 1, True)


def test_total_below_three_hundred_gets_no_discount():
    assert order_discount(299, "tuesday", True) == 0


def test_tuesday_non_student_at_minimum_total():
    assert order_discount(300, "tuesday", False) == 150


def test_tuesday_student_adds_fifty():
    assert order_discount(600, "tuesday", True) == 350


def test_saturday_non_student_gets_no_discount():
    assert order_discount(500, "saturday", False) == 0


def test_sunday_student_gets_only_student_discount():
    assert order_discount(500, "sunday", True) == 50


def test_regular_weekday_non_student_gets_ten_percent():
    assert order_discount(500, "wednesday", False) == 50


def test_regular_weekday_student_gets_extra_fifty():
    assert order_discount(500, "wednesday", True) == 100


def test_distance_over_ten_is_not_deliverable():
    assert delivery_status(15, 11) == "not deliverable"


def test_exactly_ten_kilometres_is_deliverable():
    assert delivery_status(30, 10) == "on time"


def test_thirty_one_minutes_is_late():
    assert delivery_status(31, 3) == "late"


def test_forty_five_minutes_is_still_late():
    assert delivery_status(45, 3) == "late"


def test_more_than_forty_five_minutes_gives_free_pizza():
    assert delivery_status(46, 3) == "free pizza"
