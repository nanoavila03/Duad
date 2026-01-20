#Cree una clase de User que:
#Tenga un atributo de date_of_birth.
#Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        return 2026 - self.date_of_birth

def verify_age(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError("User is not of legal age")
        return func(user)
    return wrapper

@verify_age
def login(user):
    print(f"User {user.date_of_birth} logged in")

def main():
    user1 = User(2000)
    login(user1)

    user2 = User(2010)
    try:
        login(user2)
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()