#Cree una estructura de objetos que asemeje un Double Ended Queue.
#Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def push_left(self, value):
        new_node = Node(value)
        if not self.front:  
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def push_right(self, value):
        new_node = Node(value)
        if not self.rear:  
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def pop_left(self):
        if not self.front:  
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None  
        return removed_value

    def pop_right(self):
        if not self.rear:  
            return None
        removed_value = self.rear.value
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None  
        return removed_value

    def print_deque(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Deque contents:", elements)

deque = Deque()
deque.push_left(10)
deque.push_right(20)
deque.push_left(5)
deque.print_deque()  
print(deque.pop_left())  
deque.print_deque()  
print(deque.pop_right())  
deque.print_deque()  