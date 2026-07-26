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


test_stack = Stack()
test_stack.push(10)
test_stack.push(20)
test_stack.push(30)

test_stack.print_structure()
test_stack.pop()
test_stack.print_structure()   