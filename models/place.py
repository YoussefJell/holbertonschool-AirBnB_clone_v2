#!/usr/bin/env python3
"""Place Module"""
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity, place_amenity
from os import getenv
import models


class Place(BaseModel, Base):
    """Class for Place Objects
    Attributes:

    city_id: string - empty string
    user_id: string - empty string
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list
    """
    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = list(str())
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False, back_populates='place_amenities')
    else:
        city_id = str()
        user_id = str()
        name = str()
        description = str()
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = list(str())

        @property
        def reviews(self):
            """Returns all reviews that have the same id as self.id (Place id)"""
            my_reviews = list()
            for review in models.storage.all(Review).values():
                if self.id == review.place_id:
                    my_reviews.append(review)
            return my_reviews

        @property
        def amenities(self):
            """Returns all amenities that have the same id that is in self.amenity_ids"""
            my_amenities = list()
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    my_amenities.append(amenity)
            return my_amenities

        @amenities.setter
        def amenities(self, value):
            """add amenitie to amenity_ids"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
