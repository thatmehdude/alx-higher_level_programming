#!/usr/bin/python3
import json


class Base:
    """ This class is the "base" of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes  new base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
