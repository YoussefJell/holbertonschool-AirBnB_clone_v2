#!/usr/bin/env python3
"""User Module"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
import models


class User(BaseModel, Base):
    """Class for User Objects
    Attributes:

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    __tablename__ = "users"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = str()
        password = str()
        first_name = str()
        last_name = str()
