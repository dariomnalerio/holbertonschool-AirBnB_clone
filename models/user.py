#!/usr/bin/python3
""" Module containing class User """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Representation of a User
    """
    email = ""  # user's email
    password = ""  # user's password
    first_name = ""  # user's first name
    last_name = ""  # user's last name
