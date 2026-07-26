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
            # Recorremos la cadena desde head hasta el último nodo
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            
            # Enlazamos el nuevo nodo al final de la cadena
            current_node.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
            
        popped_node = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        return popped_node.data

    def pop_right(self):
        # 1. CASO 1: La cola está vacía
        if self.head is None:
            return None
        
        # 2. CASO 2: Solo hay un único nodo (head y tail apuntan al mismo)
        if self.head.next is None:
            popped_data = self.head.data
            self.head = None
            self.tail = None
            return popped_data
        
        # 3. CASO 3: Hay más de un nodo (Búsqueda del penúltimo)
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
            
        popped_data = self.tail.data
        self.tail = current_node
        self.tail.next = None
        
        return popped_data

    def print_structure(self):
        if self.head is None:
            print("El Queue está vacío.")
            return None
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next


# --- PRUEBAS ---
if __name__ == "__main__":
    test_queue = DoubleEndedQueue()

    print("--- Prueba 1: push_left ---")
    test_queue.push_left(10)
    test_queue.push_left(20)
    test_queue.push_left(30)
    test_queue.print_structure()

    print("\n--- Prueba 2: push_right ---")
    test_queue.push_right(5)
    test_queue.push_right(1)
    test_queue.print_structure()

    print("\n--- Prueba 3: pop_left ---")
    print("Removido del inicio:", test_queue.pop_left())
    test_queue.print_structure()

    print("\n--- Prueba 4: pop_right ---")
    print("Removido del final:", test_queue.pop_right())
    test_queue.print_structure()