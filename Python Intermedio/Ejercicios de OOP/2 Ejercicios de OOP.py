# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). 
# Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
    def __init__(self, max_passengers=50):
        self.max_passengers = max_passengers
        self.passengers = []  

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} has boarded the bus. Current passengers: {len(self.passengers)}/{self.max_passengers}")
        else:
            print("The bus is full.")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger.name} has left the bus. Current passengers: {len(self.passengers)}/{self.max_passengers}")
        else:
            print(f"{passenger.name} is not on the bus.")


class Person:
    def __init__(self, name):
        self.name = name   


def main():
    bus = Bus()
    person1 = Person("Mariano")
    person2 = Person("Juan")
    person3 = Person("Pedro")
    person4 = Person("Maria")
    person5 = Person("Ana")
    person6 = Person("Luis")
    bus.add_passenger(person1)
    bus.add_passenger(person2)
    bus.add_passenger(person3)
    bus.add_passenger(person4)
    bus.add_passenger(person5)
    bus.add_passenger(person6)
    bus.remove_passenger(person1)
    bus.remove_passenger(person2)
    bus.remove_passenger(person3)
    bus.remove_passenger(person4)
    bus.remove_passenger(person5)
    bus.remove_passenger(person6)


if __name__ == "__main__":
    main()