#!/usr/bin/env python3
"""Base_model module"""
from datetime import datetime
from enum import unique
import models
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """class BaseModel that defines all common
    attributes/methods for other classes"""
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """*args, **kwargs arguments for
        the constructor of a BaseModel"""
        kwargc = len(kwargs)
        if kwargc > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """string representation of an object"""
        my_dict = self.__dict__.copy()
        if my_dict['_sa_instance_state']:
            del my_dict['_sa_instance_state']
        return f"[{self.__class__.__name__}] ({self.id}) {my_dict}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        if my_dict['_sa_instance_state']:
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Delete from model storage"""
        models.storage.delete(self)
