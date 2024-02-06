#!/usr/bin/python3

import models
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class representing the base model for other classes.

    Attributes:
        id (str): Unique identifier generated using uuid.uuid4().
        created_at (datetime): Creation timestamp.
        updated_at (datetime): Last update timestamp.

    Methods:
        save(): Updates the 'updated_at' attribute with the current datetime.
        to_dict(): Converts the instance to a dictionary for serialization.
        __str__(): Returns a string representation of the instance.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
