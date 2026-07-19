# Cree una estructura de objetos que asemeje un Binary Tree.

#     Debe incluir un método para hacer print de toda la estructura.
#     No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None 
    
  def print_structure(self, level=0, prefix="Root: "):
    # 1. Primero recorremos todo el lado derecho (se verá arriba)
      if self.right is not None:
          self.right.print_structure(level + 1, "└── R: ")
          
      # 2. Imprimimos el nodo actual con su espacio correspondiente
      print("    " * level + prefix + str(self.data))
      
      # 3. Luego recorremos el lado izquierdo (se verá abajo)
      if self.left is not None:
          self.left.print_structure(level + 1, "└── L: ")

test_tree = Node(10)
test_tree.left = Node(5) 
test_tree.right = Node(15)
test_tree.right.left = Node(16)
test_tree.right.right = Node(17) 
test_tree.right.right.right = Node(18)



test_tree.print_structure()