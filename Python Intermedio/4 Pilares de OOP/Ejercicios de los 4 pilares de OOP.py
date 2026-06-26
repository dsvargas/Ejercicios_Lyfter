'''Cree una clase de BankAccount que:

    Tenga un atributo de balance.
    Tenga un método para ingresar dinero.
    Tengo un método para retirar dinero.
    Cree otra clase que herede de esta llamada SavingsAccount que:
    Tenga un atributo de min_balance que se pueda asignar al crearla.
    Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

Cree una clase abstracta de Shape que:

    Tenga los métodos abstractos de calculate_perimeter y calculate_area.
    Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
    Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.'''

class BankAccount:
    def __init__(self):
        self.balance = 0

    def add_money(balance):
        self.balance = balance