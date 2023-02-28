""" Test for city class """
from models.city import City
import unittest

class Test_city(unittest.TestCase):

    def test_class(self):
        new_class = City()
        self.assertTrue(isinstance(new_class, City))