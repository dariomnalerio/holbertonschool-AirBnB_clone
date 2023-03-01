#!/usr/bin/python3
""" Module containing class User """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity (desirable or useful feature or facility of a place).
    """
    name = ""  # Amenity name
