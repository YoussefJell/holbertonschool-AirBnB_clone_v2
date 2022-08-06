#!/usr/bin/python3
"""Test_state module"""
from models.state import State
from models import *
import unittest
import os
from datetime import datetime


class Test_State(unittest.TestCase):
    """Test_state class"""

    def test_attributes(self):
        """Check for attributes."""
        s = State()
        self.assertEqual(str, type(s.id))
        self.assertEqual(datetime, type(s.created_at))
        self.assertEqual(datetime, type(s.updated_at))
        self.assertTrue(hasattr(s, "name"))

    def test_str(self):
        """test the str output"""
        s1 = State()
        string = f"[{s1.__class__.__name__}] ({s1.id}) {s1.__dict__}"
        self.assertEqual(str(s1), string)

    def test_save(self):
        """test if the object is saved in file"""
        s2 = State()
        s2.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(s2.id, objects[f"{s2.__class__.__name__}.{s2.id}"].id)

    def test_todict(self):
        """test if the object is converted to dict"""
        s3 = State()
        mydict = s3.to_dict()
        self.assertEqual(mydict['__class__'], 'State')
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
