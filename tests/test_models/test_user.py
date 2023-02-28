""" Test for user class """
from models.user import User
import unittest

class Test_user(unittest.TestCase):

    def test_class(self):
        new_class = User()
        self.assertTrue(isinstance(new_class, User))