#!/usr/bin/python3
""" Test for amenity class """
from models import Amenity
import unittest
from models import BaseModel
from models import storage

class Test_amenity(unittest.TestCase):

    def test_class(self):
        new_class = Amenity()
        self.assertTrue(isinstance(new_class, Amenity))
        self.assertEqual(new_class == Amenity)