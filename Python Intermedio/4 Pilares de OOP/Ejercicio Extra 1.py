"""
Cree una clase Employee con los siguientes requisitos:

    Atributos privados: _name, _salary
    Use @property y @<atributo>.setter para:
        Mostrar el nombre y el salario
        Validar que el salario nunca sea negativo
    Cree un método promote que aumente el salario un porcentaje definido
"""
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

   
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = float(value)
        else:
            raise ValueError("Error: El salario no puede ser un monto negativo.")

    
    def promote(self, percentage):
        if percentage > 0:
            increase = self._salary * (percentage / 100)
            self.salary += increase  # Usamos el setter de forma interna
            print(f"¡{self._name} ha sido promovido! Aumento del {percentage}%.")
        else:
            print(" El porcentaje de aumento debe ser mayor a cero.")


employee = Employee("Ana", 1000)
employee.promote(0.1)  # +10%

print(employee.salary)  # 1100