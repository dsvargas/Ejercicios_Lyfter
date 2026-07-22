def repeat_twice(func):
    def wrapper(*args, **kwargs):
        # Logica extra
        
        func(*args, **kwargs) # Llamada a la funcion decorada
				# Logica extra
        func(*args, **kwargs) # Llamada a la funcion decorada
    return wrapper

@repeat_twice
def say_hi(name):
    print(f"Hola, {name}")

say_hi("Dilana")