def decorator_name(func):
    def wrapper(parameters):
        # Logica extra
        func(parameters) # Llamada a la funcion decorada
				# Logica extra

    return wrapper

