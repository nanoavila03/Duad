#Cree una clase de Circle con:
#Un atributo de radius (radio).
#Un método de get_area que retorne su área.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14159 * self.radius ** 2


if __name__ == "__main__":
    circle = Circle(5)
    print(circle.get_area())
