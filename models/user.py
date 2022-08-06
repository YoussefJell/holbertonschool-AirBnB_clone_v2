#!/usr/bin/env python3
"""User Module"""
from models.base_model import BaseModel
import models


class User(BaseModel):
    """Class for User Objects
    Attributes:

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = str()
    password = str()
    first_name = str()
    last_name = str()
