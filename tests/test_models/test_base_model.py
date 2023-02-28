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
    
    def test__str__(self):
        tested_string = BaseModel()
        dictionary = "{id: (<class 'str'>) - 54e144bd-4558-4361-97c7-c8976554a0cf, created_at: (<class 'str'>) - 2023-02-28T05:48:51.176354, updated_at: (<class 'str'>) - 2023-02-28T05:48:51.176523, name: (<class 'str'>) - My First Model, my_number: (<class 'int'>) - 89, __class__: (<class 'str'>) - BaseModel}"
        str = tested_string.__str__()
        self.assertEqual(str.__str__(), dictionary)
    
    def test_the_str(self):
        test_str = BaseModel()
        expecting = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertNotEqual(str(test_str), expecting)

    def test_save(self):
        """Check what save does"""
        with self.assertRaises(AttributeError):
            BaseModel.save(["Hello, World"])
            BaseModel.save([111, 111, 111, 111])
    
    def test_thetime(self):
        """ test the actual datetime """
        test = BaseModel()
        test.save()
        time = datetime.now()
        self.assertFalse(test == time)

    
