#1
# string + string → ? funciona es concatenacion de ambos textos
# string + int → ? typeerror python no puede concatenarle a un texto un entero hay que hacer un cast para hacerlo ejemplo "Age:"+str(31)
# int + string → ? typeerror mismo caso del anterior no sabe como sumarte a un entero un texto
# list + list → ? funciona lo que hace es unir ambas listas en una sola
# string + list → ?typeError son tipos totalmente diferentes que no se pueden concatenar
# float + int → ? funciona y el entero termina cambiando de tipo a flotante
# bool + bool → ? funciona cosa curiosa En python true vale 1 y false vale 0 por eso 

#2
first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))


if age < 0:
    category = "Invalid age"
elif age <= 2:
    category = "Bebe"
elif age <= 11:
    category = "Niño"
elif age <= 14:
    category = "Pre-adolecente"
elif age <= 17:
    category = "Adolecente"
elif age <= 29:
    category = "Adulto joven"
elif age <= 64:
    category = "Adulto"
else:
    category = "Adulto mayor"

print(f"\nUsuario: {first_name} {last_name}")
print(f"Edad: {age} years old")
print(f"Categoria: {category}")

#3 Numero secreto
import random

secret_number = random.randint(1, 10) # de esta manera se ejecuta un numero secreto aleatorio distinto cada vez
guessed = False

print("\n\n--- Adivine el numero secreto (1 a 10) ---")

while not guessed:
    user_guess = int(input("Digite un numero: "))
    
    if user_guess == secret_number:
        print("Felicidades adivino el numero.")
        guessed = True
    elif user_guess > 10:
        print("Es mayor a 10 intenta de nuevo con un numero mas bajo")

    else:
     if user_guess != secret_number:
        print("Busca otro.")
   

#4
print("\n\nVamos a adivinar el numero mas alto de tres numeros, por favor digitalos")
num1 = float(input("Digite el primer numero: "))
num2 = float(input("Digite el segundo numero: "))
num3 = float(input("Digite el tercer numero: "))


if num1 >= num2 and num1 >= num3:
    highest = num1
elif num2 >= num1 and num2 >= num3:
    highest = num2
else:
    highest = num3

print(f"El numero mas alto es: {highest}")