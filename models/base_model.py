#!/usr/bin/python3
"""
Base model module
This file contains the Base Model class, which is the father class for the
upcoming subclasses
"""

from uuid import uuid4
from datetime import datetime


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
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """
        Determines what string will be displayed when print is executed on the
        instance

        Returns: The string descripting the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        Updates the object
        """
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Returns a dictionary with the object key value pairs
        """
        object_dict = self.__dict__
        object_dict["__class__"] = self.__class__.__name__
        created_at_iso = datetime.isoformat(self.created_at)
        updated_at_iso = datetime.isoformat(self.updated_at)
        object_dict["created_at"] = created_at_iso
        object_dict["updated_at"] = updated_at_iso
        return object_dict


# object1 = BaseModel()
# print(object1.to_dict())
# print(f"id: {object1.id}, type: {type(object1.id)}")
