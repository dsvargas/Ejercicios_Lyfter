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
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def pop_left(self):
    if self.head is None:
      #el queue esta vacio
      return None
    popped_node = self.head
    self.head = self.head.next
    return popped_node.data

  def pop_right(self):
    if self.head is None:
            return None
        
    popped_data = self.tail.data
      
    # CASO ESPECIAL: Solo hay 1 elemento en la estructura
    if self.head == self.tail:
        self.head = None
        self.tail = None
        return popped_data
        
    # CASO GENERAL: Más de 1 elemento (Buscamos el penúltimo nodo)
    current_node = self.head
    while current_node.next != self.tail:
        current_node = current_node.next
        
    # Desconectamos el último nodo y actualizamos el tail
    self.tail = current_node
    self.tail.next = None
    
    return popped_data

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


test_queue = DoubleEndedQueue()

print("--- Prueba 1: push_left ---")
test_queue.push_left(10)
test_queue.push_left(20)
test_queue.push_left(30)
test_queue.print_structure()  # Salida: 30 -> 20 -> 10

print("\n--- Prueba 2: push_right ---")
test_queue.push_right(5)
test_queue.push_right(1)
test_queue.print_structure()  # Salida: 30 -> 20 -> 10 -> 5 -> 1

print("\n--- Prueba 3: pop_left ---")
print("Removido del inicio:", test_queue.pop_left())  # 30
test_queue.print_structure()  # Salida: 20 -> 10 -> 5 -> 1

print("\n--- Prueba 4: pop_right ---")
print("Removido del final:", test_queue.pop_right())   # 1
test_queue.print_structure()  # Salida: 20 -> 10 -> 5