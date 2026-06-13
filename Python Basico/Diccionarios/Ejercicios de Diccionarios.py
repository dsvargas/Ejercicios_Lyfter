hotel_information  = {
    "name": "hotel la villa",
    "number_of_starts": 5,
    "rooms": [
        {
            "number": 101,
            "floor": 1,
            "price_per_night": 75.50
        },
        {
            "number": 102,
            "floor": 1,
            "price_per_night": 75.50
        },
        {
            "number": 103,
            "floor": 1,
            "price_per_night": 75.50
        }
    ]
}
# Ejemplo para mostrar cómo se vería el objeto completo
#print(hotel_information)


#1 Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

new_diccionary = {}
for index in range(len(list_a)):
    key = list_a[index]
    value = list_b[index]
    # asigno de forma dinamica la clave y el valor al nuevo diccionary
    new_diccionary[key]= value
print(new_diccionary)

#2 Cree un programa que use una lista para eliminar keys de un diccionario.
list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    #segun encuentre llaves que esten en la lista  list_of_keys elimina la informacion del diccionario
    if key in employee: 
        del employee[key]

#print(employee)