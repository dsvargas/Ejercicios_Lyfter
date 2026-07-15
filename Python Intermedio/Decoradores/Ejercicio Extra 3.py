from datetime import datetime

def log_call(func):
    print
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con parámetros: {args}, {kwargs} Date: {datetime.now()} returned: {func(*args, **kwargs)}")

        # Logica extra

        return func(*args, **kwargs) # Llamada a la funcion decorada

                # Logica extra
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        all_values = list(args) + list(kwargs.values())
        
        if not all(isinstance(x, (int, float)) for x in all_values):
            raise TypeError("Todos los parámetros deben ser números")
        return func(*args, **kwargs)
    return wrapper


@validate_numbers
@log_call
def multiply(**args):
    return args['number1'] * args['number2']

result = multiply(number1=3, number2=4)
print(f"Resultado de la multiplicación: {result}")