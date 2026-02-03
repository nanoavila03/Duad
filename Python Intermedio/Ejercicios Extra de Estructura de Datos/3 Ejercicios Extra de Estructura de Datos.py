#Lista doblemente enlazada
#Requisitos:
#Cada nodo debe tener referencia al siguiente y al anterior
#Métodos:
#append(data): Agrega al final
#prepend(data): Agrega al inicio
#delete(data): Elimina el primer nodo con ese valor
#print_forward() y print_backward(): Imprime en ambas direcciones

class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current and current.data != data:
            current = current.next
        if not current:
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def print_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

dll = DoublyLinkedList()
dll.append(10) 
dll.prepend(5)
dll.append(15)
print("Forward:")
dll.print_forward()
print("Backward:")
dll.print_backward()
dll.delete(10)
dll.print_forward()