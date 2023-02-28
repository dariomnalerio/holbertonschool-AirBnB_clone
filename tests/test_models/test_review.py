""" Test for review class """
from models.review import Review
import unittest

class Test_review(unittest.TestCase):

    def test_class(self):
        new_class = Review()
        self.assertTrue(isinstance(new_class, Review))
        self.assertIsInstance(new_class, Review)