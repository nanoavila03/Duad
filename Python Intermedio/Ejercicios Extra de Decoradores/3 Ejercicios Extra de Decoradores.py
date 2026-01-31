#Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
#A esta función se le debe combinar dos decoradores:
#@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
#@validate_numbers: revisa que todos los argumentos sean numéricos

def multiply(a, b):
    return a * b

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args}")
        return func(*args, **kwargs)
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be numbers")
        for arg in kwargs.values():
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be numbers")
        return func(*args, **kwargs)
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

def main():
    print(f'Result: {multiply(2, 3)}')

if __name__ == "__main__":
    main()
