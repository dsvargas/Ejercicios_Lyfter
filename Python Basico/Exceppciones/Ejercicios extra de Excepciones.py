#1 Pida al usuario su nombre, Luego pida su edad, Si todo sale bien, imprima un mensaje:
#Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
#Si no es un número válido, capture el ValueError y muestre un mensaje
#Si todo sale bien, imprima un mensaje:
#
def foo1():
    try:
        # 1. Ask for the name
        name = input("Enter your name: ")
        if name.isdigit():
            raise ValueError("The name cant be a number")
        
        # 2. Ask for the age (nested try-except)
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("invalid number")
            return # Stops the function immediately so it won't print the final message
            
        # 3. If everything goes well
        print("Hi {}, your age is {}".format(name, age))

    except ValueError as name_error:
        # This catches the manual error we raised for the name
        print(name_error)

#foo1()

#2 Cree una función convertir_a_entero(lista) que:
#Reciba una lista de strings, Intente convertir cada elemento a entero usando int(), Use try-except para atrapar los errores ValueError
#Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

def convert_to_integer(strings_list):
    
    for element in strings_list:
        try:
            # Try to convert the string element into an integer
            result = int(element)
            print('"{}" converted to {}'.format(element, result))
            
        except ValueError:
            # If it fails (text or decimals), catch the error
            # Show the error message and let the loop continue with the next item
            print("Could not convert element: {}".format(element))

my_list = ['4', 'hello', '10', '5.2']
#convert_to_integer(my_list)


#3 Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total#

def sum_values(mixed_list):
    total_sum = 0.0
    
    for element in mixed_list:
        try:
            # Try to convert the element into a float
            float_value = float(element)
            
            # If successful, add it to the total
            total_sum = total_sum + float_value
            print("{} successfully added".format(float_value))
            
        except ValueError:
            # If conversion fails (like 'apple' or 'n/a'), catch the error
            print("Invalid element: {}".format(element))
            
    # Print the final accumulated total after the loop finishes
    print("\nTotal sum: {}".format(total_sum))

my_list = ['10', 'manzana', '5.5', '3', 'n/a']

sum_values(my_list)