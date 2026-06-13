print("---- Simulador de Ahorro ----")

name = input("Ingresa tu nombre: ")
monthly_savings = float(input("¿Cuántos dólares ahorras por mes? "))
months = int(input("¿Cuántos meses deseas simular? "))
total = 0

for month in range(1, months + 1):
    total += monthly_savings
    print(f"Mes {month}: total acumulado = {total}")

print(f"{name}, en {months} meses habrás ahorrado: {total}")