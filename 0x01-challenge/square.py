#!/usr/bin/python3
"""
    Sqaure class
"""

class square():
    """ defines the attributes and methods of the square class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initializes a square """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the sqaure """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """ String repr of the square """
        return "{}/{}".format(self.width, width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
