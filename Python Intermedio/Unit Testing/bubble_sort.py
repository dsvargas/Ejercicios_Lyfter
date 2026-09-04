def bublesort(arr):
    n = len(arr)
    for i in range(n):
        # Bucle de DERECHA a IZQUIERDA
        # Empieza en el último índice (n - 1) y baja hasta i
        for j in range(n - 1, i, -1):
            # Comparamos el elemento de la derecha con el de su izquierda
            if arr[j] < arr[j - 1]:
                # Guardamos los valores antes de intercambiar solo para el print claro
                val_menor = arr[j]
                val_mayor = arr[j - 1]
                
                # Intercambiamos los valores
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                
                print(f"Intercambiando {val_menor} y {val_mayor}: {arr}")
    return arr


my_test_list = [64, 34, 25, 12, 22, 11, 9]
print("Lista original:", my_test_list)
print("-" * 50)

sorted_list = bublesort(my_test_list)

print("-" * 50)
print("Lista ordenada:", sorted_list)