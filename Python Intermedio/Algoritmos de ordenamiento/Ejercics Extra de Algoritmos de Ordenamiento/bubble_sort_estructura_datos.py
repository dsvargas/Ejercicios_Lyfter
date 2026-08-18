import functools

# ==========================================
# 1. DECORADOR DE VALIDACIÓN DE ENTRADA
# ==========================================
def validar_stack_para_ordenar(func):
    """
    Decorador que valida antes de ordenar:
    1. Que la entrada sea una instancia de Stack.
    2. Que el Stack no esté vacío.
    3. Que todos los datos almacenados en sus nodos sean números.
    """
    @functools.wraps(func)
    def wrapper(stack, *args, **kwargs):
        # Validar que se reciba un objeto Stack
        if not isinstance(stack, Stack):
            raise TypeError("❌ Error: Se esperaba una estructura de tipo Stack.")

        # Validar que el Stack no esté vacío
        if stack.top is None:
            raise ValueError("❌ Error: El Stack está vacío, no hay nada que ordenar.")

        # Recorrer los nodos para verificar que todos los datos sean números (excluyendo booleans)
        current = stack.top
        while current is not None:
            if isinstance(current.data, bool) or not isinstance(current.data, (int, float)):
                raise TypeError(f"❌ Error: El nodo con el valor '{current.data}' no es un número válido.")
            current = current.next

        # Si pasa todas las validaciones, ejecuta la función de ordenamiento
        return func(stack, *args, **kwargs)

    return wrapper

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node   

  def pop(self):
    if self.top is None:
      #el stack esta vacio
      return None
    popped_node = self.top
    self.top = self.top.next
    return popped_node.data
    
  def print_structure(self):
    if self.top is None:
    #el stack esta vacio
      print("El Stack está vacío.")
      return None
    else:
      current_node = self.top
      while current_node is not None:
          print(current_node.data)
          current_node = current_node.next





@validar_stack_para_ordenar
def bubble_sort_stack(stack):
    if stack.top is None:
        return
    
    pasadas= 0
    total_swaps = 0
    swapped = True
    while swapped:
        swapped = False
        pasadas += 1    

        current_node = stack.top
        while current_node is not None and current_node.next is not None:
            if current_node.data > current_node.next.data:
                # Intercambiar los datos de los nodos
                current_node.data, current_node.next.data = current_node.next.data, current_node.data
                swapped = True
                total_swaps += 1
            current_node = current_node.next

    print(f"Iteraciones: {pasadas}")
    print(f"Intercambios: {total_swaps}")
    return pasadas,total_swaps

#prueba con un stack con datos numéricos
test_stack = Stack()
test_stack.push(10)
test_stack.push(2)
test_stack.push(85)
test_stack.push(12)
test_stack.push(5)

print("--- Stack Original ")
test_stack.print_structure()

print("\n--- Ejecutando Bubble Sort ---")
bubble_sort_stack(test_stack)

print("\n--- Stack Ordenado ---")
test_stack.print_structure()

#Prueba con un stack vacío
empty_stack = Stack()

print("--- Stack Original ")
empty_stack.print_structure()

print("\n--- Ejecutando Bubble Sort ---")
bubble_sort_stack(empty_stack)

print("\n--- Stack Ordenado ---")
empty_stack.print_structure()

#Prueba con un stack con datos no numéricos
invalid_stack = Stack()
invalid_stack.push("no es un número")
invalid_stack.push(5)
invalid_stack.push(10)

print("--- Stack Original ")
invalid_stack.print_structure()

print("\n--- Ejecutando Bubble Sort ---")
bubble_sort_stack(invalid_stack)

print("\n--- Stack Ordenado ---")
invalid_stack.print_structure()
