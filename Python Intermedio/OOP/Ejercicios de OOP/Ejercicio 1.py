class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0
		age = 56

person_1 = Person("John")
age = 34

person_2 = Person("Alice")
age = 28

class Bus:
    def __init__(self, max_passangers):
        self.max_passangers = max_passangers
        self.passangers = []

    def add_passanger(self, person):
        if len(self.passangers) < self.max_passangers:
            self.passangers.append(person)
            return f"{person.name} added."
        else:
            return f"Cannot add {person.name}. Maximum capacity is {self.max_passangers}."
        
    def remove_passanger(self, person): 
        if person in self.passangers:
            self.passangers.remove(person)
            return f"{person.name} removed."
        else:
            return f"{person.name} is not in the bus."  
        
bus = Bus(2)
print(bus.add_passanger(person_1))  # Output: John added.
print(bus.add_passanger(person_2))  # Output: Alice added.
print(bus.remove_passanger(person_1))  # Output: John removed.  

