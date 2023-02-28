""" Test for place class """
from models.place import Place
import unittest

class Test_place(unittest.TestCase):

    def test_class(self):
        new_class = Place()
        self.assertTrue(isinstance(new_class, Place))
        self.assertIsInstance(new_class, Place)