#Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

#Una de las principales ventajas es que podemos reutilizar código, lo cual nos permite crear relaciones entre clases sin tener que volver a escribir los mismos métodos o atributos una y otra vez.

#Las clases nos ayudan a armar objetos a partir de un conjunto de atributos y métodos definidos de forma general. 
#Gracias a la herencia, podemos crear clases hijas que aprovechen lo que ya existe en otras clases, haciéndolas más completas o más específicas según lo que se necesite para cada caso.

#Algunos usos comunes son:

#Reutilizar funcionalidades de diferentes clases sin duplicar código.

#Combinar características independientes.

#Modelar situaciones reales donde algo pertenece a más de una categoría.

#Ejemplo:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Acelerate:
    def __init__(self, speed):
        self.speed = speed

    def accelerate(self):
        print("The vehicle is accelerating.")

class Brake:
    def __init__(self, speed):
        self.speed = speed

    def brake(self):
        print("The vehicle is braking.")


class DrivingCar(Car, Acelerate, Brake):
    def __init__(self, brand, model, speed):
        Car.__init__(self, brand, model)
        Acelerate.__init__(self, speed)
        Brake.__init__(self, speed)
    
    def model_car(self):
        print("The vehicle is a", self.brand, self.model)

    def accelerate(self):
        print("The vehicle is accelerating.")

    def brake(self):
        print("The vehicle is braking.")

    def drive(self):
        print("The vehicle is driving.")

driving_car = DrivingCar("Tesla", "Model X", 1000)
driving_car.accelerate()
driving_car.brake()
driving_car.drive()
driving_car.model_car()