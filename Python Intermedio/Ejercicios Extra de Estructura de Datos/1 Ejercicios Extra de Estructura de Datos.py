#Cree una estructura que represente una cola básica (Queue) con objetos enlazados
#Restricción:
#no usar list, dict, tuple, collections
#Métodos requeridos:
#enqueue(data): agrega un nodo al final
#dequeue(): elimina y retorna el nodo del inicio
#print_all(): imprime todos los elementos de la cola en orden

class Node:
    data: str
    next: 'Node'

    def __init__(self, data: str):
        self.data = data
        self.next = None

class Queue:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data: str):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def dequeue(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_data

    def print_all(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


queue = Queue()
queue.enqueue("Element 1") 
queue.enqueue("Element 2")  
queue.enqueue("Element 3")  
print("Dequeuing:", queue.dequeue())
queue.print_all()