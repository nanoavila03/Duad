#1.Implemente un bubble_sort que funcione 
#La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso
#2.Conteo de pasos (bubble_sort_steps)
#Modifique su implementación de bubble_sort para que:
#Cuente cuántas iteraciones (pasadas) realiza el algoritmo
#Cuente cuántos intercambios se hicieron en total
#3.Validación de entrada antes de ordenar
#Cree una función que reciba una lista y valide:
#Que todos los elementos sean números
#Que no esté vacía
#Luego aplique bubble_sort si pasa las validaciones
#Si hay error, debe lanzar un mensaje apropiado

class Node:
    data: str
    next: "Node"
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node
    
    def __init__(self, head):
        self.head = head

def get_length(linked_list):
    count = 0
    current = linked_list.head
    while current:
        count += 1
        current = current.next
    return count

def bubble_sort(linked_list):
    if not linked_list.head:
        return linked_list
    
    n = get_length(linked_list)
    
    for i in range(n):
        current = linked_list.head
        prev = None
        
        for j in range(n - i - 1):
            next_node = current.next
            
            if current.data > next_node.data:
                current.next = next_node.next
                next_node.next = current
                
                if prev:
                    prev.next = next_node
                else:
                    linked_list.head = next_node
                
                prev = next_node
            else:
                prev = current
                current = next_node
    
    return linked_list

def bubble_sort_steps(linked_list):
    if not linked_list.head:
        return linked_list, 0, 0
    
    n = get_length(linked_list)
    iterations = 0
    swaps = 0
    
    for i in range(n):
        iterations += 1
        current = linked_list.head
        prev = None
        
        for j in range(n - i - 1):
            next_node = current.next
            
            if current.data > next_node.data:
                swaps += 1
                current.next = next_node.next
                next_node.next = current
                
                if prev:
                    prev.next = next_node
                else:
                    linked_list.head = next_node
                
                prev = next_node
            else:
                prev = current
                current = next_node
    
    return linked_list, iterations, swaps

def validate_and_sort(linked_list):
    if not linked_list.head:
        return "Error: The list is empty."
    
    current = linked_list.head
    while current:
        if not isinstance(current.data, (int, float, str)):
            return "Error: All elements must be valid data types."
        current = current.next
    
    return bubble_sort(linked_list)

def print_linked_list(linked_list):
    current = linked_list.head
    result = []
    while current:
        result.append(str(current.data))
        current = current.next
    return " -> ".join(result)

node5 = Node(90)
node4 = Node(11, node5)
node3 = Node(22, node4)
node2 = Node(12, node3)
node1 = Node(64, node2)
my_list = LinkedList(node1)

print("Original:")
print(print_linked_list(my_list))

sorted_list = validate_and_sort(my_list)
if isinstance(sorted_list, str):
    print(sorted_list)
else:
    print("\nSorted:")
    print(print_linked_list(sorted_list))

node_a = Node("Tercer nodo")
node_b = Node("Segundo nodo", node_a)
node_c = Node("Primer nodo", node_b)
my_list2 = LinkedList(node_c)

print("\n\nOriginal (strings):")
print(print_linked_list(my_list2))

sorted_list2, iterations, swaps = bubble_sort_steps(my_list2)
print(f"\nSorted: {print_linked_list(sorted_list2)}")
print(f"Iterations: {iterations}")
print(f"Swaps: {swaps}")

empty_list = LinkedList(None)
print("\n\nEmpty list validation:")
print(validate_and_sort(empty_list))