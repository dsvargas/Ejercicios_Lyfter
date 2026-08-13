class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def insert_front(self, new_data):
        """Inserta un nuevo nodo al frente de la lista."""
        new_node = LinkedListNode(new_data)
        new_node.next = self
        if self.prev:
            self.prev.next = new_node
            new_node.prev = self.prev
        self.prev = new_node
        return new_node  # Retorna el nuevo nodo como el nuevo head

    def insert_back(self, new_data):
        """Inserta un nuevo nodo al final de la lista."""
        new_node = LinkedListNode(new_data)
        new_node.prev = self
        if self.next:
            self.next.prev = new_node
            new_node.next = self.next
        self.next = new_node
        return new_node  # Retorna el nuevo nodo como el nuevo tail

    def delete(self, data):
        """Elimina el nodo con el dato especificado de la lista."""
        current = self
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                # Desconecta el nodo actual
                current.prev = None
                current.next = None
                return
            current = current.next
        # Desconecta el nodo actual
        self.prev = None
        self.next = None

    def print_all(self):
        """Imprime todos los nodos desde este nodo hacia adelante."""
        current = self
        while current:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
        print("None")

ll = LinkedListNode(1)
print("Lista inicial:")
ll.print_all()  # [1] -> None

# REASIGNAMOS 'll' al insertar al frente
ll = ll.insert_front(10)
ll = ll.insert_front(20)
print("\nDespués de insertar 10 y 20 al frente:")
ll.print_all()  # [20] -> [10] -> [1] -> None

print("\nDespués de insertar 30 al final del nodo 1:")
# Para insertar al final, navegamos hasta el último nodo
tail = ll
while tail.next:
    tail = tail.next
tail.insert_back(30)

ll.print_all()  # [20] -> [10] -> [1] -> [30] -> None

print("\nDespués de eliminar el nodo con valor 10:")
ll.delete(10)
ll.print_all()  # [20] -> [1] -> [30] -> None