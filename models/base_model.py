#!/usr/bin/python3
""" Module containing class BaseModel """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for all other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance variables
        """
        if len(kwargs) > 0:
            format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, item in kwargs.items():
                if key == 'id':
                    self.id = str(item)
                if key == 'created_at':
                    self.created_at = datetime.strptime(item, format)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(item, format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return string representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dictionary version of "__dict__"
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
