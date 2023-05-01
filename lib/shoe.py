#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=None, color=None, material=None):
        self.brand = brand
        self._size = size
        self._color = color
        self._material = material
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("Size must be an integer")
        else:
            self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            print("Color must be a string")
        else:
            self._color = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, str):
            print("Material must be a string")
        else:
            self._material = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    # def __init__(self, size, material, condition):
    #     self.size = size
    #     self.material = material
    #     self.condition = condition

    # def shoe_size(self, value):

    #     if type(value) != int:
    #         print("size must be an integer")
        
