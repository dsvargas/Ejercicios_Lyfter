def requires_login(func):
    def wrapper(parameters):
        # Logica extra
        if not user_logged_in:
            print("Debe iniciar sesión para ver su perfil")
            return
        func(parameters) # Llamada a la funcion decorada
				# Logica extra

    return wrapper

    user_logged_in = False

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")