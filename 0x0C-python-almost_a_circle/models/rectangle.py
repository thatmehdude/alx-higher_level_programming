#!/usr/bin/python3
"""defines a rectangle class"""

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
