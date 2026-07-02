#Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def decorator_name(func):
    def wrapper(parameters):
        print(f"Parámetros: {parameters}")
        result = func(parameters)
        return result
    return wrapper

@decorator_name
def funtion_name(parameters):
    return parameters


funtion_name(5)


#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def decorator_check_numbers(func):
    def wrapper(*parameters):
        # Logica extra
        for param in parameters:
            if not isinstance(param, (int, float)):
                raise TypeError("Todos los parámetros deben ser números")
        func(*parameters) # Llamada a la funcion decorada
				# Logica extra

    return wrapper


@decorator_check_numbers
def my_function_with_infinite_params(*args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

my_function_with_infinite_params(2, 5, 6, 5, 6, 5, 6)
my_function_with_infinite_params(2, 5, 6, "k", 6, 5, 6)