'''
Cree una clase abstracta de Shape que:

    Tenga los métodos abstractos de calculate_perimeter y calculate_area.
    Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
    Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.'''


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = float(side)

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return self.side * 4

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)

    def calculate_area(self):
        return self.base * self.height

    def calculate_perimeter(self):
        return 2 * (self.base + self.height)



circle1 = Circle(5)
square2 = Square(4)
rectangle1 = Rectangle(5, 3)

print(f"Círculo    -> Área: {circle1.calculate_area():.2f} | Perímetro: {circle1.calculate_perimeter():.2f}")
print(f"Cuadrado   -> Área: {square2.calculate_area():.2f} | Perímetro: {square2.calculate_perimeter():.2f}")
print(f"Rectángulo -> Área: {rectangle1.calculate_area():.2f} | Perímetro: {rectangle1.calculate_perimeter():.2f}")