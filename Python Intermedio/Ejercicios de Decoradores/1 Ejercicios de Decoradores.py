#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

class cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"
    
def entry_cars(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@entry_cars
def show_cars(car, Made_in, color):
    print(f"The car is from {Made_in} and the color is {color}")
    return car

def main():
    car = cars("Toyota", "Corolla", 2022)
    show_cars(car, Made_in="Japan", color="Blue")

if __name__ == "__main__":
    main()
