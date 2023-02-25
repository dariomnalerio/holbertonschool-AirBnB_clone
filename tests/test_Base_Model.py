#usr/bin/python3
""" unittest for Class BaseModel """
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime

class Test_BaseModel(unittest.TestCase):

    def test_actual_time(self):
        my_model = BaseModel()
        my_model.save()
        time = datetime.now()
        self.assertFalse(my_model.updated_at == time)