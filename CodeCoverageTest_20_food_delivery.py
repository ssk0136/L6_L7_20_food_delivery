import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


@pytest.mark.parametrize("distance,value,raining,expected", [
    (2, 200, False, 20),
    (3, 300, True, 50),
    (6, 300, False, 40),
    (10, 200, False, 60),
    (15, 500, True, 30),
    (1, 500, False, 0)
])
def test_delivery_charge(distance, value, raining, expected):
    assert delivery_charge(distance, value, raining) == expected


@pytest.mark.parametrize("distance", [0, -1, 15.1])
def test_invalid_distance(distance):
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(distance, 200, False)


@pytest.mark.parametrize("value,code,first,expected", [
    (300, None, False, 300),
    (300, "SAVE50", False, 250),
    (300, "WELCOME", True, 200),
    (100, "SAVE50", False, 100)
])
def test_coupons(value, code, first, expected):
    assert apply_coupon(value, code, first) == expected


@pytest.mark.parametrize("code,first,message", [
    ("BAD", False, "invalid coupon"),
    ("WELCOME", False, "coupon only for first order")
])
def test_invalid_coupons(code, first, message):
    with pytest.raises(ValueError, match=message):
        apply_coupon(300, code, first)


@pytest.mark.parametrize("peak,busy,expected", [
    (False, False, 23),
    (True, False, 33),
    (False, True, 38),
    (True, True, 53)
])
def test_estimated_time(peak, busy, expected):
    assert estimated_time(2, peak, busy) == expected
