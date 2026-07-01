'''
    Cree una clase base Vehicle con los atributos:
        _brand
        _year

Agregue un método get_info() que devuelva una descripción del vehículo.
Luego cree dos clases hijas:

    Car
    Motorcycle

Cada una debe agregar su propio atributo (por ejemplo, doors o type) y sobrescribir el método get_info() para incluir esta información adicional.
'''
class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Marca: {self._brand}, Año: {self._year}"


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return f"Marca: {self._brand}, Año: {self._year}, Puertas: {self._doors}" 

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return f"Marca: {self._brand}, Año: {self._year}, Tipo: {self._type}"
    

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")


print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
print(vehicle2.get_info())  # Yamaha (2022) - Tipo: Deportiva