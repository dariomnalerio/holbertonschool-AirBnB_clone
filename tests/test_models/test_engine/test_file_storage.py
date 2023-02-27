#!/usr/bin/python3
""" Test Filestorage """
import unittest
from os import path
from models import storage
from models.engine.file_storage import FileStorage

class Test_File_Storage(unittest.TestCase):
    """ Doc """    
    
    def empty_class(self):
        """ empty """
    
    def test_empty(self):
        """ test empty class  """
        self.assertNotEqual(storage.all(), {})
    
    def test_all(self):
        """ check  all function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)