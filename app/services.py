from app.models import Booking
from app.db import SessionLocal
from app.validators import validate_booking_data

def create_booking(data):
    validate_booking_data(data)
    db = SessionLocal()
    try:
        booking = Booking(
            firstname=data["firstname"],
            lastname=data["lastname"],
            totalprice=data["totalprice"],
            depositpaid=data["depositpaid"],
            bookingdates=data["bookingdates"]
        )
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking.to_dict()
    finally:
        db.close()

def get_booking(booking_id):
    db = SessionLocal()
    try:
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        return booking.to_dict() if booking else None
    finally:
        db.close()

def update_booking(booking_id, data):
    validate_booking_data(data)
    db = SessionLocal()
    try:
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            return None

        booking.firstname = data["firstname"]
        booking.lastname = data["lastname"]
        booking.totalprice = data["totalprice"]
        booking.depositpaid = data["depositpaid"]
        booking.bookingdates = data["bookingdates"]

        db.commit()
        db.refresh(booking)
        return booking.to_dict()
    finally:
        db.close()

def delete_booking(booking_id):
    db = SessionLocal()
    try:
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            return False
        db.delete(booking)
        db.commit()
        return True
    finally:
        db.close()