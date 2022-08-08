#!/usr/bin/env python3
"""City Module"""
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
from os import getenv
import models


class City(BaseModel, Base):
    """Class for City Objects
    Attributes:

    state_id: string - empty string
    name: string - empty string
    """
    __tablename__ = "cities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(
            "states.id"), nullable=False, )
    else:
        state_id = str()
        name = str()
