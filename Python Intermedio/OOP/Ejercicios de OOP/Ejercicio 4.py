
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
circulo = Circle(5)
print(circulo.area())  # Output: 78.5