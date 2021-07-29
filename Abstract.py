# to abstract methods must import libs
from abc import ABC, abstractmethod

# Abstract class will be created
# this class is hidden from the user
# this class parameter will be ABC ( abstract base classes)
# ABC is imported and must be used to abstract the class
class Shape(ABC):
    # add decorator @abstractmethod
    # @abstractmethod claims the method as an abstract method
    # MUST be used in child class once claimed as a abstract method

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


# subclasses
class Square(Shape):
    # initializer must be created
    def __init__(self, side):
        self.side = side

    # abstract method from shape is being used
    def area(self):
        return self.side * self.side

    # abstract method from shape is being used
    def perimeter(self):
        return 4 * self.side

# subclass created
square = Square(5)
print(square.area())
print(square.perimeter())
