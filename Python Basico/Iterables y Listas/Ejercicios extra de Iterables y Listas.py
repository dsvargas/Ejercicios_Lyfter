#1 Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar
# Lista de ejemplo y número a buscar
my_list = [4, 2, 7, 2, 8, 2, 1]
numero_a_buscar = 2

contador = 0

for num in my_list:
    if num == numero_a_buscar:
        contador += 1
q
print("El número {} aparece {} veces".format(numero_a_buscar, contador))
#2 Cree un programa que verifique si todos los elementos de una lista son positivos
my_list = [3, 6, 0, -2, 4]

todos_positivos = True

for num in my_list:
    if num <= 0:
        todos_positivos = False
        break  # Ya no hace falta seguir revisando el resto

if todos_positivos:
    print("Todos los números son positivos")
else:
    print("Hay al menos un número negativo o cero")
#3 Cree un programa que muestre el valor más pequeño de una lista sin usar min().
my_list = [9, 4, 7, 1, 5]

# Empezamos asumiendo que el primero es el menor de todos
menor = my_list[0]

for num in my_list:
    if num < menor:
        menor = num

print("El menor valor es {}".format(menor))
#4 Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio
my_list = [10, 20, 30, 40, 50]

# 1. Calcular el promedio
suma_total = 0
for num in my_list:
    suma_total += num

promedio = suma_total / len(my_list)

# 2. Filtrar los mayores al promedio
mayores_al_promedio = []
for num in my_list:
    if num > promedio:
        mayores_al_promedio.append(num)

print("Promedio: {}".format(promedio))
print("Nueva lista: {}".format(mayores_al_promedio))
#5 Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
palabras_ingresadas = []

# 1. Solicitar las 5 palabras al usuario
for i in range(5):
    palabra = input("Ingrese la palabra {}: ".format(i + 1))
    palabras_ingresadas.append(palabra)

# 2. Filtrar las que tienen más de 4 letras
palabras_largas = []
for palabra in palabras_ingresadas:
    if len(palabra) > 4:
        palabras_largas.append(palabra)

print("\nNueva lista filtrada:")
print(palabras_largas)