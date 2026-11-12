from hypothesis import given, strategies as st
from ride_share_fare import parse_trip, fare_average, payable_fare

@given(st.text() | st.none())
def test_parse_trip_no_crash(s):
    """Fuzz parse_trip with arbitrary text, including missing input."""
    parse_trip(s)

@given(st.text() | st.none())
def test_fare_average_no_crash(s):
    """Fuzz fare_average with arbitrary CSV-like text and missing input."""
    fare_average(s)

@given(st.text() | st.none())
def test_payable_fare_no_crash(s):
    """Fuzz payable_fare with arbitrary text and missing input."""
    payable_fare(s)
