# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"
 
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Make a noise"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"

dog = Dog("Bob")
cat = Cat("Chispas")

print(dog.speak())
print(cat.speak())