#!/usr/bin/python3
""" Test Filestorage """
import unittest
from os import path
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class Test_File_Storage(unittest.TestCase):
    """ Doc """    
    
    def empty_class(self):
        """ empty """
    
    def test_empty(self):
        """ test empty class  """
        self.assertNotEqual(storage.all(), {})
    
    def test_functios(self):
        """ check  all function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)
    
    def test_save_function(self):
        """ Save  """
        test = BaseModel()
        key = 'BaseModel' + '.' + test.id
        self.assertEqual(test, storage.all()[key])

    def test_reload_function(self):
        """ Reload"""
        test = BaseModel()
        key = 'BaseModel' + '.' + test.id
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertTrue(key in storage.all().keys())
        self.assertEqual(test.id, storage.all()[key].id)