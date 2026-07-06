"""

Cree una clase de User que:

    Tenga un atributo de date_of_birth.
    Tenga un property de age.
    Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
"""
import datetime
class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        # Implementación para calcular la edad basada en date_of_birth
        today = datetime.date.today()
        calculated_age = today.year - self.date_of_birth.year
        return calculated_age

def check_adult(func):
    def wrapper(user, *arg, **kwargs):
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad")
        return func(user, *arg, **kwargs)

    return wrapper


@check_adult
def rent_vehicle(user):
    print(" puede alquilar un vehículo.")


def hacer_prueba():
    # Creamos un usuario mayor de edad y uno menor de edad
    adulto = User( datetime.date(1998, 5, 15))
    menor = User( datetime.date(2012, 10, 20))

    print(f"--- Evaluando (Edad: {adulto.age} años) ---")
    rent_vehicle(adulto)

    print(f"--- Evaluando (Edad: {menor.age} años) ---")
    rent_vehicle(menor)

hacer_prueba()