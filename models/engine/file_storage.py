#!/usr/bin/python3
"""FileStorage Module"""
from json import dumps, loads
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class FileStorage that
    serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = dict()

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict

        return self.__objects

    def count(self, cls=None):
        """Counts how many instances exist"""
        if cls is not None:
            cls = eval(cls)
            count = 0
            for k, v in self.__objects.items():
                if type(v) == cls:
                    count += 1
            return count
        return 0

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_json = dict()
        for key, value in self.__objects.items():
            my_json[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            my_file.write(dumps(my_json))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)"""
        if exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                my_json = loads(my_file.read())
                for key, value in my_json.items():
                    self.__objects[key] = eval(value['__class__'])(**value)

    def delete(self, obj=None):
        """to delete obj from __objects if it's inside
        if obj is equal to None, the method should not do anything"""
        if obj:
            my_obj = "{}.{}".format(type(obj).__name__, obj.id)
            if self.__objects[my_obj]:
                del self.__objects[my_obj]
                self.save()

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
