"""
**super() called within a class method gives you access to the parent object
**super() can alsi be called with parameters indicating the class and object
to access
        *super(class, object)


"""


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# using inheritance and super
class New_Square(Rectangle):
    # reinitialize child class the class needs only 1 argument
    def __init__(self, length):
        # super allows access to the parents methods
        # pass in squares length -> for both parents arguments (length, width)
        super().__init__(length, length)


class Cube(New_Square):
    def surface_area(self):
        # using parent methods still
        face_area = self.area()
        return face_area

    def volume(self):
        # using parents methods still
        face_area = super.area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return 'Triangle'


# TODO MULTIPLE INHERITANCE
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return ' Right Pyramid '
