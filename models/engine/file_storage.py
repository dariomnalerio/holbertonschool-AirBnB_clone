#!/usr/bin/python3
""" Module containing class FileStorage """
import json
from os import path


class FileStorage:
    """
    Serialize instances to a JSON file
    and deserialize JSON file to instances
    """

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        Returns all saved objects in dictionary format
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict.update({key: value.to_dict()})

        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        """
        from models.base_model import BaseModel

        if not path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, mode='r') as f:
            obj_dict = json.load(f)
            FileStorage.__objects = {}
            for key, value in obj_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)
