#!/usr/bin/python3
"""Base module."""

class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): If provided, assign it to the instance id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
