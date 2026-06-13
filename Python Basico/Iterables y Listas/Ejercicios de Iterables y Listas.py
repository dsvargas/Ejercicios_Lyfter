#1 Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(len(first_list)):
    print(f'{first_list[index]} {second_list[index]}')


#2 Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
my_string = 'Pizza con piña'

#range(inicio, fin, paso)
for index in range(len(my_string) -1,-1,-1):
    print(my_string[index])

    
#3 Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list = [4, 3, 6, 1, 7]
#3.1 Intercambio directo usando el índice 0 y el índice -1
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
#3.2 Usando una variable temporal
temporal = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temporal
print(my_list)

#4 Cree un programa que elimine todos los números impares de una lista.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range (len(my_list) -1, -1, -1):
    if my_list[index] % 2 != 0:
        my_list.remove(my_list[index])
        
print(my_list)
      

#5 Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
numbers = []
for i in range(10):
    num = int(input("Input the number " + str(i + 1) + ":  "))
    numbers.append(num)

higher_number = max(numbers)
print("The number in the list are: " + str(numbers))
print("The higher number is: " + str(higher_number))