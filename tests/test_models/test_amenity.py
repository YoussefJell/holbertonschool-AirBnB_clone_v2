#!/usr/bin/env python3
"""Test_Amenity module"""
from models.amenity import Amenity
from models import *
import unittest
import os
from datetime import datetime


class Test_Amenity(unittest.TestCase):
    """Test_Amenity class"""

    def test_attributes(self):
        """Check for attributes."""
        a = Amenity()
        self.assertEqual(str, type(a.id))
        self.assertEqual(datetime, type(a.created_at))
        self.assertEqual(datetime, type(a.updated_at))
        self.assertTrue(hasattr(a, "name"))

    def test_str(self):
        """test the str output"""
        a1 = Amenity()
        string = f"[{a1.__class__.__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(str(a1), string)

    def test_save(self):
        """test if the object is saved in file"""
        a2 = Amenity()
        a2.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(a2.id, objects[f"{a2.__class__.__name__}.{a2.id}"].id)

    def test_todict(self):
        """test if the object is converted to dict"""
        a3 = Amenity()
        mydict = a3.to_dict()
        self.assertEqual(mydict['__class__'], 'Amenity')
        self.assertEqual(type(mydict['created_at']), str)
        self.assertEqual(type(mydict['updated_at']), str)

    @classmethod
    def tearDownClass(cls):
        """City testing teardown.
        Delete the FileStorage
        """
        try:
            os.remove("file.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
