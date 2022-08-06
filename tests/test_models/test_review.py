#!/usr/bin/env python3
"""Test_Review module"""
from models.review import Review
from models import *
import unittest
import os
from datetime import datetime


class Test_Review(unittest.TestCase):
    """Test_Review class"""

    def test_attributes(self):
        """Check for attributes."""
        r = Review()
        self.assertEqual(str, type(r.id))
        self.assertEqual(datetime, type(r.created_at))
        self.assertEqual(datetime, type(r.updated_at))
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))

    def test_str(self):
        """test the str output"""
        r1 = Review()
        string = f"[{r1.__class__.__name__}] ({r1.id}) {r1.__dict__}"
        self.assertEqual(str(r1), string)

    def test_save(self):
        """test if the object is saved in file"""
        r2 = Review()
        r2.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(r2.id, objects[f"{r2.__class__.__name__}.{r2.id}"].id)

    def test_todict(self):
        """test if the object is converted to dict"""
        r3 = Review()
        mydict = r3.to_dict()
        self.assertEqual(mydict['__class__'], 'Review')
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
