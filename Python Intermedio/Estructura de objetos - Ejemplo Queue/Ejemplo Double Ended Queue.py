# Cree una estructura de objetos que asemeje un Double Ended Queue.

#     Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
#     Debe incluir un método para hacer print de toda la estructura.
#     No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class DoubleEndedQueue:
  def __init__(self):
    self.head = None
    self.tail = None

  def push_left(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node

  def push_right(self, data):
    new_node = Node(data)
    new_node.next = self.tail
    self.tail = new_node
  

  def pop_left(self):
    if self.head is None:
      #el queue esta vacio
      return None
    popped_node = self.head
    self.head = self.head.next
    return popped_node.data

  def pop_right(self):
    if self.tail is None:
      #el queue esta vacio
      return None
    popped_node = self.tail
    # Encontrar el nodo anterior al tail
    current_node = self.head
    while current_node.next != self.tail:
      current_node = current_node.next
    self.tail = current_node
    self.tail.next = None
    return popped_node.data

  def print_structure(self):
    if self.head is None:
    #el queue esta vacio
      print("El Stack está vacío.")
      return None
    else:
      current_node = self.head
      while current_node is not None:
          print(current_node.data)
          current_node = current_node.next


test_stack = DoubleEndedQueue()
test_stack.push_left(10)
test_stack.push_left(20)
test_stack.push_left(30)
test_stack.print_structure()
print("El Stack está vacío.")
test_stack.push_right(10)
test_stack.push_left(20)
test_stack.push_right(30)
test_stack.print_structure()
print("El Stack está vacío.")
test_stack.push_left(10)
test_stack.push_right(20)
test_stack.push_left(30)
test_stack.print_structure()
print("El Stack está vacío.")


test_stack.pop_left()
test_stack.print_structure()   