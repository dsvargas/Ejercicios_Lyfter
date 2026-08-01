class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None  # Puntero al inicio de la cola (para remover)
        self.tail = None  # Puntero al final de la cola (para agregar)

    def enqueue(self, data):
        """Agrega un elemento al final de la cola (push)."""
        new_node = Node(data)
        
        # Si la cola está vacía, el nuevo nodo es tanto el head como el tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Enlazamos el último nodo actual al nuevo nodo y actualizamos tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """Remueve y retorna el elemento al frente de la cola (pop)."""
        if self.head is None:
            print("⚠️ La cola está vacía.")
            return None
        
        # Guardamos el dato del frente
        popped_data = self.head.data
        
        # Movemos el frente al siguiente nodo
        self.head = self.head.next
        
        # Si la cola quedó vacía tras remover, limpiamos también el tail
        if self.head is None:
            self.tail = None
            
        return popped_data

    def peek(self):
        """Muestra el elemento al frente sin removerlo."""
        if self.head is None:
            return None
        return self.head.data

    def print_structure(self):
        """Imprime la estructura completa desde el frente hacia el final."""
        if self.head is None:
            print("La cola está vacía.")
            return
        
        current_node = self.head
        print("Frente ->", end=" ")
        while current_node is not None:
            print(f"[{current_node.data}]", end=" -> ")
            current_node = current_node.next
        print("Final")


# ==========================================
# 🧪 BLOQUE DE PRUEBAS
# ==========================================
if __name__ == "__main__":
    cola = Queue()

    print("--- 1. Encolando elementos (enqueue) ---")
    cola.enqueue("Cliente 1")
    cola.enqueue("Cliente 2")
    cola.enqueue("Cliente 3")
    cola.print_structure()

    print("\n--- 2. Consultando el frente (peek) ---")
    print("Siguiente a ser atendido:", cola.peek())

    print("\n--- 3. Desencolando elementos (dequeue) ---")
    print("Atendiendo a:", cola.dequeue())  # Sale 'Cliente 1'
    cola.print_structure()

    print("Atendiendo a:", cola.dequeue())  # Sale 'Cliente 2'
    cola.print_structure()

    print("\n--- 4. Encolando un nuevo cliente ---")
    cola.enqueue("Cliente 4")
    cola.print_structure()

    print("\n--- 5. Vaciando la cola ---")
    cola.dequeue()  # Sale 'Cliente 3'
    cola.dequeue()  # Sale 'Cliente 4'
    cola.print_structure()