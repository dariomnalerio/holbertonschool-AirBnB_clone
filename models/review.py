#!/usr/bin/python3
""" Module containing class User """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Representation of a Review for a service
    """
    place_id = ""  # The ID of the Place object being reviewed
    user_id = ""  # The ID of the User object who wrote the review
    text = ""  # The text content of the review
