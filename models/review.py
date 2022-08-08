#!/usr/bin/env python3
"""Review Module"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from os import getenv
import models


class Review(BaseModel, Base):
    """Class for Review Objects
    Attributes:

    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string
    """
    __tablename__ = "reviews"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(
            "places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey(
            "users.id"), nullable=False)
    else:
        place_id = str()
        user_id = str()
        text = str()

        @property
        def reviews(self):
            """Returns all reviews that have the same id as self.id (State id)"""
            my_reviews = list()
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    my_cities.append(city)
            return my_cities
