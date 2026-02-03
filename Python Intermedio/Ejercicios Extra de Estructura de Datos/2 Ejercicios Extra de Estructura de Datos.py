#Cree una clase LinkedList con los métodos:
#insert_front(data): Inserta al inicio
#insert_back(data): Inserta al final
#delete(data): Elimina el primer nodo con el valor dado
#print_all(): Imprime todos los valores

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if not current:
            return
        if previous:
            previous.next = current.next
        else:
            self.head = current.next

    def print_all(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        

ll = LinkedList()   
ll.insert_back(10)
ll.insert_front(5)
ll.insert_back(15)
ll.print_all() 
ll.delete(10)
ll.print_all()  

