import math


def parse_trip(text):
    """Parse a ``cab:distance`` trip; return an empty trip for invalid input."""
    if not isinstance(text, str):
        return "", 0.0

    parts = text.split(':')
    if len(parts) != 2:
        return "", 0.0

    cab, km_text = (part.strip() for part in parts)
    if not cab:
        return "", 0.0
    try:
        km = float(km_text)
    except (ValueError, OverflowError):
        return "", 0.0
    if not math.isfinite(km) or km < 0:
        return "", 0.0

    return cab.title(), km

def fare_average(fares_csv):
    """Return the integer average, or zero when the CSV input is invalid."""
    if not isinstance(fares_csv, str):
        return 0

    parts = fares_csv.split(',')
    if not parts or any(not part.strip() for part in parts):
        return 0
    try:
        values = [int(part.strip()) for part in parts]
    except (ValueError, OverflowError):
        return 0
    if any(value < 0 for value in values):
        return 0
    return sum(values) // len(values)

def payable_fare(text):
    """Calculate the payable fare, or zero when the input is invalid."""
    if not isinstance(text, str):
        return 0.0

    parts = text.split('|')
    if len(parts) != 2:
        return 0.0
    fare_text, promo_text = (part.strip() for part in parts)
    try:
        fare = float(fare_text)
        promo = float(promo_text)
    except (ValueError, OverflowError):
        return 0.0
    if (not math.isfinite(fare) or fare < 0 or
            not math.isfinite(promo) or promo < 0):
        return 0.0

    total = fare * 1.18 - promo
    return max(total, 0)

def main():
    print("==== Running parse_trip ====")
    user_input = input("Enter cab:distance in km (e.g. sedan:12): ")
    result = parse_trip(user_input)
    print("Cab and Distance:", result)

    print("\n==== Running fare_average ====")
    user_input = input("Enter fares as CSV (e.g. 120,95,210): ")
    result = fare_average(user_input)
    print("Average Fare:", result)

    print("\n==== Running payable_fare ====")
    user_input = input("Enter fare|promo (e.g. 250|30): ")
    result = payable_fare(user_input)
    print("Payable Fare:", result)

if __name__ == "__main__":
    main()
