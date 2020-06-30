#!/usr/bin/python3
""" first unit testing file for basemodel """


import unittest
from models.base_model import BaseModel
import uuid
import json
from datetime import datetime as dt


class TestBase(unittest.TestCase):
    """unit testing class"""

    def test_bm1(self):
        """basic test for some attributes """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.created_at, dt)
        self.assertIsInstance(b.updated_at, dt)
        self.assertNotIsInstance(b.id, uuid.UUID)
        self.assertIsInstance(b.id, str)

    def test_bm2(self):
        """second set of testing for baseModel"""
        bm2 = BaseModel()
#        #bm2.id = "1"
        strep = "[{}] ({}) {}".format(type(bm2).__name__, bm2.id, bm2.__dict__)
        self.assertEqual(str(bm2), strep)

    def test_bm3(self):
        """testing to_dict"""
        bm3 = BaseModel()
        cdict = {}
        cdict['__class__'] = "BaseModel"
        cdict["created_at"] = str(bm3.created_at.isoformat())
        cdict["updated_at"] = str(bm3.updated_at.isoformat())
        cdict["id"] = bm3.id
        self.assertEqual(cdict, bm3.to_dict())