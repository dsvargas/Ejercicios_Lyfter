user_logged_in = False
def requires_login(func):
    def wrapper(*args, **kwargs):
        # Logica extra
        if not user_logged_in:
            raise ValueError("Debe iniciar sesión para ver su perfil")
            
        return func(*args, **kwargs) # Llamada a la funcion decorada
				
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


def test():
    
    try:
        
        print("--- Intento 1: Con user_logged_in = False ---")
        view_profile()
    except ValueError as error:
        print(f"Excepción atrapada con éxito: {error}")


test()