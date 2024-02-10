#!/usr/bin/python3

import models
import uuid
from datetime import datetime
from models.engine.file_storage import storage

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
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Unused arguments.
            **kwargs: Keyword arguments representing attribute name-value pairs.
                      Each key is an attribute name, and each value is the value of that attribute.
                      If 'kwargs' is not empty, it recreates the instance from the dictionary representation.
                      Otherwise, it creates a new instance with generated 'id' and 'created_at'.

        Note:
            'created_at' and 'updated_at' attributes are converted from string to datetime objects.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        and save the instance to the storage.
        """
        self.updated_at = datetime.now()
        storage.save()

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
