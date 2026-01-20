#Cree un decorador @requires_login que:
#Verifique si la variable global user_logged_in es True
#Si no lo es, debe lanzar una excepción "Usuario no autenticado"
#Si lo es, la función decorada se ejecuta normalmente

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise ValueError("User not authenticated")
        return func(*args, **kwargs)
    return wrapper

user_logged_in = True

@requires_login
def view_profile():
    print("Viewing profile")

def main():
    global user_logged_in
    
    user_logged_in = False
    print("User not logged in")
    try:
        view_profile()
    except ValueError as e:
        print(f"Error: {e}")
    
    user_logged_in = True
    print("User logged in")
    try:
        view_profile()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()