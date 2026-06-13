sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name': 'Iron', 'upc': 'ITEM-324', 'unit_price': 32.45},
            {'name': 'Basketball', 'upc': 'ITEM-432', 'unit_price': 12.54}
        ]
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name': 'Key Holder', 'upc': 'ITEM-23', 'unit_price': 5.42}
        ]
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {'name': 'Key Holder', 'upc': 'ITEM-23', 'unit_price': 3.42},
            {'name': 'Basketball', 'upc': 'ITEM-432', 'unit_price': 17.54}
        ]
    }
]

# Diccionario donde acumularemos los totales
result = {}

# 1. Primer ciclo: recorremos cada orden de venta
for sale in sales:
    # 2. Segundo ciclo: recorremos la lista de ítems dentro de esa venta
    for item in sale['items']:
        codigo_upc = item['upc']
        precio = item['unit_price']
        
        # Si el código UPC no está en el diccionario, lo registramos empezando en 0
        if codigo_upc not in result:
            result[codigo_upc] = 0.0
            
        # Sumamos el precio al total acumulado de ese producto
        # Usamos round() opcionalmente a 2 decimales para evitar imprecisiones de flotantes
        result[codigo_upc] = round(result[codigo_upc] + precio, 2)

# Imprimimos el resultado final
print(result)


#2

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

# Diccionario vacío para organizar los grupos
empleados_por_departamento = {}

# Recorremos cada empleado de la lista
for emp in employees:
    depto = emp["department"]
    nombre = emp["name"]
    
    # Si el departamento aún no existe en el diccionario, 
    # lo agregamos con una lista vacía
    if depto not in empleados_por_departamento:
        empleados_por_departamento[depto] = []
        
    # Agregamos el nombre del empleado a la lista de ese departamento
    empleados_por_departamento[depto].append(nombre)

# Imprimimos el resultado
print(empleados_por_departamento)




#3

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

# Diccionario vacío para acumular los totales
totales_por_categoria = {}

# Recorremos cada producto de la lista
for prod in products:
    categoria = prod["category"]
    precio = prod["price"]
    
    # Si la categoría no está en el diccionario, la inicializamos en 0
    if categoria not in totales_por_categoria:
        totales_por_categoria[categoria] = 0
        
    # Sumamos el precio al acumulado de esa categoría
    totales_por_categoria[categoria] = totales_por_categoria[categoria] + precio

# Imprimimos el resultado final
print(totales_por_categoria)


