class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Puntero al nodo anterior

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Puntero al inicio de la lista
        self.tail = None  # Puntero al final de la lista

    def append(self, data):
        """Agrega un elemento al final de la lista."""
        new_node = Node(data)
        
        if self.head is None:
            # Si la lista está vacía, el nuevo nodo es tanto head como tail
            self.head = new_node
            self.tail = new_node
        else:
            # Enlazamos el nuevo nodo al final de la lista
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Agrega un elemento al inicio de la lista."""
        new_node = Node(data)
        
        if self.head is None:
            # Si la lista está vacía, el nuevo nodo es tanto head como tail
            self.head = new_node
            self.tail = new_node
        else:
            # Enlazamos el nuevo nodo al inicio de la lista
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        """Remueve el primer nodo que contiene el dato especificado."""
        current_node = self.head
        
        while current_node is not None:
            if current_node.data == data:
                # Si es el nodo head
                if current_node == self.head:
                    self.head = current_node.next
                    if self.head is not None:
                        self.head.prev = None
                # Si es el nodo tail
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    # Nodo en medio de la lista
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                
                return True  # Nodo removido exitosamente
            
            current_node = current_node.next
        
        return False  # Nodo no encontrado

    def print_forward(self):
        """Imprime la estructura completa desde el inicio hacia el final."""
        if self.head is None:
            print("La lista está vacía.")
            return
        
        current_node = self.head
        print("Inicio ->", end=" ")
        while current_node is not None:
            print(f"[{current_node.data}]", end=" -> ")
            current_node = current_node.next
        print("Final")
            
    def print_backward(self):
        """Imprime la estructura completa desde el final hacia el inicio."""
        if self.tail is None:
            print("La lista está vacía.")
            return
        
        current_node = self.tail
        print("Final ->", end=" ")
        while current_node is not None:
            print(f"[{current_node.data}]", end=" -> ")
            current_node = current_node.prev
        print("Inicio")