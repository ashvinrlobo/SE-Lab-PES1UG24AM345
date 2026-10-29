import pytest
from ride_share_fare import extra_distance_fare, seats_and_bags_ok, pickup_status

# Example test cases:
def test_within_included_distance():
    assert extra_distance_fare("sedan", 5, "city", False) == 0

def test_seats_and_bags_ok():
    assert seats_and_bags_ok(2, 1, False) is True

# Write the rest of the test cases so that the code is 90-100% covered.
#Line Coverage
def test_unknown_cab_type():
    with pytest.raises(ValueError, match="unknown cab type"):
        extra_distance_fare("bike", 10, "city", False)


def test_negative_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        extra_distance_fare("sedan", -1, "city", False)


def test_subscriber_discount():
    assert extra_distance_fare("sedan", 10, "city", True) == 0


def test_extra_distance_city():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_extra_distance_outstation():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90


def test_long_outstation_trip():
    assert extra_distance_fare("mini", 30, "outstation", False) == 750


def test_wheelchair_passenger_limit():
    assert seats_and_bags_ok(2, 3, True) is True
    assert seats_and_bags_ok(3, 1, True) is False


def test_passenger_limit():
    assert seats_and_bags_ok(5, 1, False) is False


def test_bag_limit():
    assert seats_and_bags_ok(2, 3, False) is False


def test_pickup_on_time():
    assert pickup_status(10, True, False) == "on_time"


def test_pickup_delayed():
    assert pickup_status(3, False, False) == "delayed"


def test_pickup_missed():
    assert pickup_status(-11, False, False) == "missed"


def test_airport_pickup():
    assert pickup_status(15, False, True) == "on_time"

#Branch Coverage
def test_long_city_trip():
    assert extra_distance_fare("mini", 30, "city", False) == 500
