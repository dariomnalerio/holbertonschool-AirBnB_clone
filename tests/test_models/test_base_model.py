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

    def test_to_dict(self):
        diccionary = BaseModel()
        dict = diccionary.to_dict()
        self.assertEqual(dict['id'], diccionary.id)
        self.assertEqual(dict['created_at'], diccionary.created_at.isoformat())
        self.assertEqual(dict['updated_at'], diccionary.updated_at.isoformat())
        self.assertEqual(dict['__class__'], 'BaseModel')
    
    def test_str(self):
        test_str = BaseModel()
        expecting = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertAlmostEqual(str(test_str), expecting)

    def test_save(self):
        """Check what save does"""
        with self.assertRaises(AttributeError):
            BaseModel.save(["Hello, World"])