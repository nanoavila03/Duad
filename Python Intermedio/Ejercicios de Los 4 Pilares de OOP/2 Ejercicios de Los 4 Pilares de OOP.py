#Cree una clase abstracta de Shape que:
#Tenga los métodos abstractos de calculate_perimeter y calculate_area.
#Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
#Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)

print("Circle:")
print("Perimeter:", circle.calculate_perimeter())
print("Area:", circle.calculate_area())

print("\nSquare:")
print("Perimeter:", square.calculate_perimeter())
print("Area:", square.calculate_area())

print("\nRectangle:")
print("Perimeter:", rectangle.calculate_perimeter())
print("Area:", rectangle.calculate_area())
