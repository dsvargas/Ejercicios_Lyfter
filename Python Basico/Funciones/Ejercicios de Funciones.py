#1 Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def second_function():
    print("Hello world from the second function!")

def first_function():
    print("Hello from the first function!")
    second_function()  # Calling the second one
      

#first_function()

#2 Experimente con el concepto de scope:
#  Intente acceder a una variable definida dentro de una función desde afuera. 
#  Intente acceder a una variable global desde una función y cambiar su valor.
def my_function():
    local_var = "inside the funtion"

my_function()
# print(local_var)  # ❌ This will crash! NameError: name 'local_var' is not defined

x = 10  # Global variable

def modify_global():
    global x 
    x = 20    

#modify_global()
#print("Global x is now:" + str(x))  # Prints 20

#3 Cree una función que retorne la suma de todos los números de una lista.
def sum_list_elements(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

# Test
my_list = [4, 6, 2, 29]
result = sum_list_elements(my_list)
#print("The sum is: " + str(result))  # 41

#4 Cree una función que le dé la vuelta a un string y lo retorne.
def reverse_string(text):
    reversed_text = ""
    
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    return reversed_text

# Test
original = "Hola mundo"
result = reverse_string(original)
#print(result)  # "odnum aloH"


#5 Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
def count_cases(text):
    upper_count = 0
    lower_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print("There's {} upper cases and {} lower cases".format(upper_count, lower_count))

# Test
#count_cases("La zaguata Rompio la Caja")


#6 Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
def sort_separate_hyphen_words(text):
    
    word_list = text.split('-')
    
    
    word_list.sort()
    
    # Join the list back into a string using hyphens
    sorted_text = '-'.join(word_list)
    
    return sorted_text

# Test
input_text = "python-variable-funcion-computadora-monitor"
result = sort_separate_hyphen_words(input_text)
#print(result)


#7 Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
def is_prime(num):
    if num <= 1:
        return False 
    
    for i in range(2, num):
        if num % i == 0:
            return False #the primes are only divisible by one or itsself
            
    return True  

def filter_primes(numbers_list):
    prime_list = []
    for num in numbers_list:
        # We call our helper function here
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# Test
my_numbers = [1, 4, 6, 7, 13, 9, 67,71]
result = filter_primes(my_numbers)
print(result)  # [7, 13, 67]

