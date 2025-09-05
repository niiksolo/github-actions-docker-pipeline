import pytest
from app.validators import validate_booking_data

def test_valid_data():
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-09-10",
            "checkout": "2025-09-12"
        }
    }
    assert validate_booking_data(data) == True

@pytest.mark.parametrize("data, error_msg", [
    (
        {"lastname": "Doe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-09-10", "checkout": "2025-09-12"}},
        "Missing required field: firstname"
    ),
    (
        {"firstname": "", "lastname": "Doe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-09-10", "checkout": "2025-09-12"}},
        "Invalid firstname"
    ),
    (
        {"firstname": "John", "lastname": "Doe", "totalprice": -5, "depositpaid": True, "bookingdates": {"checkin": "2025-09-10", "checkout": "2025-09-12"}},
        "Total price must be a non-negative integer"  # Исправлено здесь
    ),
    (
        {"firstname": "John", "lastname": "Doe", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2025-09-12", "checkout": "2025-09-10"}},
        "Checkin date must be before checkout"
    ),
])
def test_invalid_data(data, error_msg):
    with pytest.raises(ValueError) as e:
        validate_booking_data(data)
    assert error_msg in str(e.value)