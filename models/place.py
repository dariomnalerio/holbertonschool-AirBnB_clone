#!/usr/bin/python3
""" Module containing class User """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place
    """
    city_id = ""            # City id where the place is located
    user_id = ""            # User id who created the place
    name = ""               # Name of the place
    description = ""        # Description of the place
    number_rooms = 0        # Number of rooms in the place
    number_bathrooms = 0    # Number of bathrooms in the place
    max_guest = 0           # Maximum number of guests allowed in the place
    price_by_night = 0      # Price per night for the place
    latitude = 0.0          # Latitude coordinate of the place's location
    longitude = 0.0         # Longitude coordinate of the place's location
    amenity_ids = ""        # List of amenity ids associated with the place
