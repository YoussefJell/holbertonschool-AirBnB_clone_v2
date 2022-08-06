#!/usr/bin/env python3
"""Review Module"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """Class for Review Objects
    Attributes:

    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string
    """
    place_id = str()
    user_id = str()
    text = str()
