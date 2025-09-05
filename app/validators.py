def validate_booking_data(data: dict):
    required_fields = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    if not isinstance(data["firstname"], str) or not data["firstname"].strip():
        raise ValueError("Invalid firstname")

    if not isinstance(data["lastname"], str) or not data["lastname"].strip():
        raise ValueError("Invalid lastname")

    if not isinstance(data["totalprice"], int) or data["totalprice"] < 0:
        raise ValueError("Total price must be a non-negative integer")

    if not isinstance(data["depositpaid"], bool):
        raise ValueError("Depositpaid must be a boolean")

    dates = data["bookingdates"]
    if not isinstance(dates, dict):
        raise ValueError("Bookingdates must be a dictionary")

    if "checkin" not in dates or "checkout" not in dates:
        raise ValueError("Missing checkin or checkout in bookingdates")

    # Проверим, что даты — строки в формате YYYY-MM-DD
    from datetime import datetime

    try:
        checkin_date = datetime.strptime(dates["checkin"], "%Y-%m-%d")
        checkout_date = datetime.strptime(dates["checkout"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Dates must be in YYYY-MM-DD format")

    if checkin_date >= checkout_date:
        raise ValueError("Checkin date must be before checkout")

    return True
