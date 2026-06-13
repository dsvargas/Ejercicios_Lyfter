# --- Definición de Variables ---
total_de_notas = 0
contador_de_nota = 1
nota_actual = 0

cantidad_de_notas_aprobadas = 0
cantidad_de_notas_desaprobadas = 0

promedio_de_notas_aprobadas = 0
promedio_de_notas_desaprobadas = 0
promedio_de_notas_total = 0

# --- Entrada de datos inicial ---
total_de_notas = int(input("Ingrese la cantidad de notas: "))

# --- Ciclo Principal (Mientras que) ---
while contador_de_nota <= total_de_notas:
    # Mostramos el número de nota dinámico usando f-strings
    nota_actual = float(input(f"Ingrese la nota numero {contador_de_nota}: "))
    
    # Lógica de clasificación (Si / Sino)
    if nota_actual < 70:
        cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas + 1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
        
    # Acumulador para el promedio total
    promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)
    
    # Importante: avanzar el contador para que el ciclo no sea infinito
    contador_de_nota = contador_de_nota + 1

# --- Cálculo de Promedios Finales ---
# Validamos que las cantidades sean mayores a 0 para evitar divisiones entre cero
if cantidad_de_notas_desaprobadas > 0:
    promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas = 0

if cantidad_de_notas_aprobadas > 0:
    promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas
else:
    promedio_de_notas_aprobadas = 0

# --- Mostrar Resultados ---
print("\n--------------------------------------------------")
print("El estudiante tiene esta cantidad de notas aprobadas")
print(cantidad_de_notas_aprobadas)

print("Este es el promedio de notas aprobadas")
print(f"{promedio_de_notas_aprobadas:.2f}")

print("El estudiante tiene esta cantidad de notas desaprobadas")
print(cantidad_de_notas_desaprobadas)

print("Este es el promedio de notas desaprobadas")
print(f"{promedio_de_notas_desaprobadas:.2f}")

print("Este es el promedio total de notas")
print(f"{promedio_de_notas_total:.2f}")
print("--------------------------------------------------")