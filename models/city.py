#!/usr/bin/python3
""" Module containing class City """
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city
    """
    state_id = ""  # State id that the city belongs to
    name = ""  # Name of the city
