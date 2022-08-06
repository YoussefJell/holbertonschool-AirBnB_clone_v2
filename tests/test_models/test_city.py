#!/usr/bin/env python3
"""Test_City module"""
from models.city import City
from models import *
import unittest
from datetime import datetime
import os


class Test_City(unittest.TestCase):
    """Test_City class"""

    def test_attributes(self):
        """Check for attributes."""
        c = City()
        self.assertEqual(str, type(c.id))
        self.assertEqual(datetime, type(c.created_at))
        self.assertEqual(datetime, type(c.updated_at))
        self.assertTrue(hasattr(c, "name"))
        self.assertTrue(hasattr(c, "state_id"))

    def test_str(self):
        """test the str output"""
        c1 = City()
        string = f"[{c1.__class__.__name__}] ({c1.id}) {c1.__dict__}"
        self.assertEqual(str(c1), string)

    def test_save(self):
        """test if the object is saved in file"""
        c2 = City()
        c2.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(c2.id, objects[f"{c2.__class__.__name__}.{c2.id}"].id)

    def test_todict(self):
        """test if the object is converted to dict"""
        c3 = City()
        mydict = c3.to_dict()
        self.assertEqual(mydict['__class__'], 'City')
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
