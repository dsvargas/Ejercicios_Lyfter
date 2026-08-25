def manual_add(number):
    result = 0 # O(1)
    for i in range(1, number + 1): # O(n)
        result += i # O(1)
    return result # O(1)
  
def add_formula(number):
    return number * (number + 1) // 2 # O(1)

    """Preguntas:

    ¿Cuál es la complejidad de cada versión?
    El primer algoritmo es O(n), tiene que iterar por todos los números y el segundo es O(1) tiene una complejidad constante.

    ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
    usaria el segundo algoritmo, ya que es mucho más eficiente y rápido, ya que no tiene que iterar por todos los números, sino que realiza una operación matemática directa.
    """

def linear_search(my_list, target):
    for item in my_list: # O(n)
        if item == target:
            return True
    return False

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2 # O(log n)
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
"""Preguntas:

    ¿Cuál es la complejidad de cada algoritmo?
    el primer algoritmo es O(n), ya que tiene que iterar por todos los elementos de la lista, mientras que el segundo algoritmo es O(log n), ya que divide la lista en mitades en cada iteración.
    ¿En qué condiciones conviene usar cada uno?
    si la lista está ordenada, conviene usar el segundo algoritmo, ya que es mucho más eficiente y rápido, mientras que si la lista no está ordenada, conviene usar el primer algoritmo, ya que no requiere que la lista esté ordenada.
    ¿Qué pasa si la lista no está ordenada?
    la búsqueda binaria no funcionará correctamente si la lista no está ordenada, ya que depende de la propiedad de orden para dividir la lista en mitades y descartar la mitad incorrecta. En ese caso, se debe usar la búsqueda lineal.

"""
def print_all_pairs(my_dict):
    for key1 in my_dict: # O(n)
        for key2 in my_dict: # O(n)
            print(f"{key1}-{key2}")

"""Preguntas:

    ¿Cuál es la complejidad temporal?
    La complejidad temporal es O(n^2), ya que hay dos bucles anidados que recorren el diccionario.
    ¿Cuanto dura si hay 1 millón de claves?
    
    Si hay 1 millón de claves, la duración sería proporcional a 1 millón al cuadrado, es decir, 1 billón de iteraciones. Esto puede llevar un tiempo considerable dependiendo del hardware y la eficiencia del código.
    """