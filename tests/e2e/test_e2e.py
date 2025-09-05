import pytest
from app.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_create_and_get_booking(client):
    booking_data = {
        "firstname": "Alice",
        "lastname": "Smith",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-09-10",
            "checkout": "2025-09-15"
        }
    }

    # Создаем бронирование
    response = client.post("/booking", json=booking_data)
    assert response.status_code == 200
    response_data = response.get_json()
    assert "bookingid" in response_data
    booking_id = response_data["bookingid"]

    # Получаем бронирование по id
    get_response = client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 200
    get_data = get_response.get_json()

    # Проверяем данные бронирования
    assert get_data["firstname"] == booking_data["firstname"]
    assert get_data["lastname"] == booking_data["lastname"]
    assert get_data["totalprice"] == booking_data["totalprice"]
    assert get_data["depositpaid"] == booking_data["depositpaid"]
    assert get_data["bookingdates"] == booking_data["bookingdates"]

    # Проверка несуществующего бронирования
    NON_EXISTENT_ID = 9999
    bad_response = client.get(f"/booking/{NON_EXISTENT_ID}")
    assert bad_response.status_code == 404
    assert bad_response.get_json() == {"error": "Booking not found"}