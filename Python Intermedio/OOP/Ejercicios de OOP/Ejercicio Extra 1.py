class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    # Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado
    def set_width(self, width):
        if width < 0:
            raise ValueError("Width cannot be negative.")
        self.width = width

    def set_height(self, height):
        if height < 0:
            raise ValueError("Height cannot be negative.")
        self.height = height


#rectangle.set_width(-3)  # This will raise a ValueError
print(rectangle.area())
print(rectangle.perimeter())

def create_rectangle():
    width = int()
    rectangle = Rectangle()
    rectangle.set_width(250)
    rectangle.set_height(300)