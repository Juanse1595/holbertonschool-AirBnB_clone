#!/usr/bin/python3
"""
Base model module
This file contains the Base Model class, which is the father class for the
upcoming subclasses
"""

from uuid import uuid4


class BaseModel:
    """
    BaseModel class
    Defines all common attributes and methos for the rest of the classes
    """
    def __init__(self) -> None:
        """
        Constructor method for BaseModel class
        """
        self.id = str(uuid4())


object1 = BaseModel()
print(object1)
print(f"id: {object1.id}, type: {type(object1.id)}")