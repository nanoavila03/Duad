#Cree una estructura de objetos que asemeje un Binary Tree.
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = self.right
            self.right = new_node

    def print_tree(self, level=0):
        if self.right is not None:
            self.right.print_tree(level + 1)
        print(' ' * 4 * level + '->', self.value)
        if self.left is not None:
            self.left.print_tree(level + 1)

if __name__ == "__main__":
    root = Node(10)
    root.insert_left(5)
    root.insert_right(15)
    root.left.insert_left(3)
    root.left.insert_right(7)
    root.right.insert_right(20)

    root.print_tree()