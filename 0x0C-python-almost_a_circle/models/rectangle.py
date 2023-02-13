#!/usr/bin/python3


class Rectangle(Base):
    """the rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialiser"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get/set width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the ara of the rectangle"""
        return self.width * self.height

    def display(self):
        """returns a visual representation of the rctangle
        The rectangle is represented with the # character"""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns the string representation of the rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}". format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
