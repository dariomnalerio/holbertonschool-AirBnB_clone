""" Test for state class """
from models.state import State
import unittest

class Test_state(unittest.TestCase):

    def test_class(self):
        new_class = State()
        self.assertTrue(isinstance(new_class, State))