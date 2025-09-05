from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    totalprice = Column(Integer, nullable=False)
    depositpaid = Column(Boolean, nullable=False)
    bookingdates = Column(JSON, nullable=False)  # json with checkin and checkout

    def to_dict(self):
        return {
            "bookingid": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": self.bookingdates
        }