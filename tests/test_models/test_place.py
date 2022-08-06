#!/pr/bin/env python3
"""Test_Place module"""
from models.place import Place
from models import *
import unittest
import os
from datetime import datetime


class Test_Place(unittest.TestCase):
    """Test_Place class"""

    def test_attributes(self):
        """Check for attributes."""
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertEqual(datetime, type(p.created_at))
        self.assertEqual(datetime, type(p.updated_at))
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "description"))
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "latitude"))
        self.assertTrue(hasattr(p, "longitude"))

    def test_str(self):
        """test the str output"""
        p1 = Place()
        string = f"[{p1.__class__.__name__}] ({p1.id}) {p1.__dict__}"
        self.assertEqual(str(p1), string)

    def test_save(self):
        """test if the object is saved in file"""
        p2 = Place()
        p2.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(p2.id, objects[f"{p2.__class__.__name__}.{p2.id}"].id)

    def test_todict(self):
        """test if the object is converted to dict"""
        p3 = Place()
        mydict = p3.to_dict()
        self.assertEqual(mydict['__class__'], 'Place')
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
