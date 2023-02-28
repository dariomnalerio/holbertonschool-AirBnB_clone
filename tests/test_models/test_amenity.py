#!/usr/bin/python3
""" Test for amenity class """
from models.amenity import Amenity
import unittest

class Test_amenity(unittest.TestCase):

    def test_class(self):
        new_class = Amenity()
        self.assertTrue(isinstance(new_class, Amenity))