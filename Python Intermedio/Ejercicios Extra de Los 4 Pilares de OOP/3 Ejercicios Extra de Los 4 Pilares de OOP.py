#Cree una clase base Vehicle con los atributos:
#_brand
#_year
#Agregue un método get_info() que devuelva una descripción del vehículo.
#Luego cree dos clases hijas:
#Car
#Motorcycle
#Cada una debe agregar su propio atributo (por ejemplo, doors o type) y sobrescribir el método get_info() para incluir esta información adicional.

class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}, Doors: {self._doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}, Type: {self._type}"

def main():
    Vehicle1 = Car("Toyota", 2022, 4)
    Vehicle2 = Motorcycle("Ducati", 2021, "Sport")
    print(Vehicle1.get_info())
    print(Vehicle2.get_info())

if __name__ == "__main__":
    main()  