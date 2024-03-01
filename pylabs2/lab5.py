class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        if value < node.value:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                self._add_node(value, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self._add_node(value, node.right_child)

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, node):
        if node is not None:
            self._traverse(node.left_child)
            print(node.value)
            self._traverse(node.right_child)

#Перевірка
#tree = BinaryTree()
#tree.add_node(5)
#tree.add_node(3)
#tree.add_node(7)
#tree.add_node(1)
#tree.add_node(9)

#tree.traverse() # Виведе 1 3 5 7 9