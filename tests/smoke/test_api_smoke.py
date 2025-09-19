import pytest
from app.main import create_app
from app.models import Base
from app.db import engine

@pytest.fixture(scope="module")
def client():

    Base.metadata.create_all(bind=engine)

    app = create_app()
    client = app.test_client()

    yield client


    Base.metadata.drop_all(bind=engine)

def test_smoke_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200

def test_smoke_booking_post_get(client):
    booking = {
        "firstname": "Smoke",
        "lastname": "Test",
        "totalprice": 50,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-09-01",
            "checkout": "2025-09-03"
        }
    }
    post_resp = client.post("/booking", json=booking)
    assert post_resp.status_code == 200, post_resp.get_data(as_text=True)

    booking_id = post_resp.get_json()["bookingid"]
    get_resp = client.get(f"/booking/{booking_id}")
    assert get_resp.status_code == 200