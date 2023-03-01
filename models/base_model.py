#!/usr/bin/python3
""" Module containing class BaseModel """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for all other classes

    Attributes:
        id (str): Unique identifier for the object.
        created_at (datetime): Date and time the object was created.
        updated_at (datetime): Date and time the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        If kwargs is not empty, sets the attributes of the instance using
        the keys and values in kwargs.

        Otherwise, sets the id, created_at, and updated_at attributes to
        default values and adds the instance to the storage.
        """
        if len(kwargs) > 0:
            # If kwargs is not empty, recreate
            # the object from a dictionary representation.
            format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, item in kwargs.items():
                if key == 'id':
                    self.id = str(item)
                if key == 'created_at':
                    self.created_at = datetime.strptime(item, format)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(item, format)
        else:
            # If kwargs is empty, create a new object.
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute of the instance to the current
        datetime and saves the instance to the storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
