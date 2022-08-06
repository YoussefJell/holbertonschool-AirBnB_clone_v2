#!/usr/bin/env python3
"""City Module"""
from models.base_model import BaseModel
import models


class City(BaseModel):
    """Class for City Objects
    Attributes:

    state_id: string - empty string
    name: string - empty string
    """
    state_id = str()
    name = str()
