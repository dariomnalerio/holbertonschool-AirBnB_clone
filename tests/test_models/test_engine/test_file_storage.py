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
        test1 = User()
        key_1 = 'User' + '.' +   test1.id
        test2 = City()
        key_2 = 'City' + '.' + test2.id
        test3 = Amenity()
        key_3 = 'Amenity' + '.' + test3.id
        test4 = Place()
        key_4 = 'Place' + '.' + test4.id
        test5 = Review()
        key_5 = 'Review' + '.' + test5.id
        test6 = State()
        key_6 = 'State' + '.' + test6.id
        self.assertEqual(test, storage.all()[key])
        self.assertEqual(test1, storage.all()[key_1])
        self.assertEqual(test2, storage.all()[key_2])
        self.assertEqual(test3, storage.all()[key_3])
        self.assertEqual(test4, storage.all()[key_4])
        self.assertEqual(test5, storage.all()[key_5])
        self.assertEqual(test6, storage.all()[key_6])

    def test_reload_function(self):
        """ Reload"""
        test = BaseModel()
        key = 'BaseModel' + '.' + test.id
        test1 = User()
        key_1 = 'User' + '.' +   test1.id
        test2 = City()
        key_2 = 'City' + '.' + test2.id
        test3 = Amenity()
        key_3 = 'Amenity' + '.' + test3.id
        test4 = Place()
        key_4 = 'Place' + '.' + test4.id
        test5 = Review()
        key_5 = 'Review' + '.' + test5.id
        test6 = State()
        key_6 = 'State' + '.' + test6.id
        storage.save()
        self.assertTrue(path.isfile('storage.json'))
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertTrue(key in storage.all().keys())
        self.assertEqual(test.id, storage.all()[key].id)
        self.assertTrue(key_1 in storage.all().keys())
        self.assertEqual(test1.id, storage.all()[key_1].id)
        self.assertTrue(key_2 in storage.all().keys())
        self.assertEqual(test2.id, storage.all()[key_2].id)
        self.assertTrue(key_3 in storage.all().keys())
        self.assertEqual(test3.id, storage.all()[key_3].id)
        self.assertTrue(key_4 in storage.all().keys())
        self.assertEqual(test4.id, storage.all()[key_4].id)
        self.assertTrue(key_5 in storage.all().keys())
        self.assertEqual(test5.id, storage.all()[key_5].id)
        self.assertTrue(key_6 in storage.all().keys())
        self.assertEqual(test6.id, storage.all()[key_6].id)