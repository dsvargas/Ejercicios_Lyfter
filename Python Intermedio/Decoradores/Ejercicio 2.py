"""

Cree una clase de User que:

    Tenga un atributo de date_of_birth.
    Tenga un property de age.
    Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
"""

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        # Implementación para calcular la edad basada en date_of_birth
        calculated_age = today.year - self.date_of_birth.year
        return calculated_age

def check_adult(func):
    def wrapper(user, *arg, **kwargs):
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad")
        return func(user, *arg, **kwargs)

    return wrapper