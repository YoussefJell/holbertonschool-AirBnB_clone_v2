#!/usr/bin/env python3
"""Place Module"""
from models.base_model import BaseModel
import models


class Place(BaseModel):
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
