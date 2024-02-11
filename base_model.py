#!/usr/bin/python3

import models
from uuid import uuid4
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
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Unused arguments.
            **kwargs: Keyword arguments representing
                      attribute name-value pairs.
                      Each key is an attribute name, and each value is
                      the value of that attribute.
                      If 'kwargs' is not empty, it recreates the instance
                      from the dictionary representation.
                      Otherwise, it creates a new instance
                      with generated 'id' and 'created_at'.

        Note:
            'created_at' and 'updated_at' attributes are converted
             from string to datetime objects.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        and save the instance to the storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

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
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
