#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def verify_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be numbers")
        
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise ValueError("All arguments must be numbers")
        
        return func(*args, **kwargs)
    return wrapper

@verify_numbers
def login(user_id, password):
    print(f"User {user_id} logged in")

def main():
    user1 = 12345
    password = 9876
    login(user1, password)  

    user2 = "John"
    password2 = 1234
    try:
        login(user2, password2)  
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()