class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def speak(self):
        print("Hace un sonido")

class Dog(Animal):
    def speak(self):
       return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"

        
dog = Dog("Fido")
cat = Cat("Whiskers")
dog.speak()
cat.speak()