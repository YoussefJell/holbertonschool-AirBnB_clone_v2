#!/usr/bin/env python3
"""Amenity Module"""
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """Class for Amenity Objects
    Attributes:

    name: string - empty string
    """
    __tablename__ = "cities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = str()
