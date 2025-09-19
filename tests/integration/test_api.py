import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    return app.test_client()

def test_update_and_delete_booking(client):
    booking = {
        "firstname": "Old",
        "lastname": "Data",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-09-10",
            "checkout": "2025-09-12"
        }
    }


    post_resp = client.post("/booking", json=booking)
    assert post_resp.status_code == 200, f"POST failed: {post_resp.data}"
    data = post_resp.get_json()
    assert "bookingid" in data, "Response missing bookingid"
    booking_id = data["bookingid"]


    updated_data = {
        "firstname": "New",
        "lastname": "Name",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-09-11",
            "checkout": "2025-09-13"
        }
    }
    put_resp = client.put(f"/booking/{booking_id}", json=updated_data)
    assert put_resp.status_code == 200, f"PUT failed: {put_resp.data}"

    put_json = put_resp.get_json()
    assert "booking" in put_json, "PUT response missing booking"
    assert put_json["booking"]["firstname"] == "New"
    assert put_json["booking"]["totalprice"] == 150


    delete_resp = client.delete(f"/booking/{booking_id}")
    assert delete_resp.status_code == 200, f"DELETE failed: {delete_resp.data}"
    assert delete_resp.get_json() == {"status": "deleted"}


    get_resp = client.get(f"/booking/{booking_id}")
    assert get_resp.status_code == 404, f"GET after delete should 404, got {get_resp.status_code}"