# Cree una estructura de objetos que asemeje un Stack.

#     Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
#     Debe incluir un método para hacer print de toda la estructura.
#     No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
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

def bubble_sort_stack(stack):
    if stack.top is None:
        return

    swapped = True
    while swapped:
        swapped = False
        current_node = stack.top
        while current_node is not None and current_node.next is not None:
            if current_node.data > current_node.next.data:
                # Intercambiar los datos de los nodos
                current_node.data, current_node.next.data = current_node.next.data, current_node.data
                swapped = True
            current_node = current_node.next
