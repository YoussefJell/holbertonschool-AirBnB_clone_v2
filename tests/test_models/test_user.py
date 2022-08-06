#!/usr/bin/env python3
"""Test_user module"""
from models.user import User
from models import *
import unittest
import os
from datetime import datetime


class Test_User(unittest.TestCase):
    """Test_user class"""

    def test_attributes(self):
        """Check for attributes."""
        u = User()
        self.assertEqual(str, type(u.id))
        self.assertEqual(datetime, type(u.created_at))
        self.assertEqual(datetime, type(u.updated_at))
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

    def test_str(self):
        """test the str output"""
        u1 = User()
        string = f"[{u1.__class__.__name__}] ({u1.id}) {u1.__dict__}"
        self.assertEqual(str(u1), string)

    def test_save(self):
        """test if the object is saved in file"""
        u2 = User()
        u2.save()
        storage.reload()
        objects = storage.all()
        self.assertEqual(u2.id, objects[f"{u2.__class__.__name__}.{u2.id}"].id)

    def test_todict(self):
        """test if the object is converted to dict"""
        u3 = User()
        mydict = u3.to_dict()
        self.assertEqual(mydict['__class__'], 'User')
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
