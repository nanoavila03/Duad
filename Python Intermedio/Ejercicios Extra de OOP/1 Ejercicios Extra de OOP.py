# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

        
def main():
    try:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        
        rect = Rectangle(width, height)
        print(f"Area: {rect.get_area()}")
        print(f"Perimeter: {rect.get_perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    