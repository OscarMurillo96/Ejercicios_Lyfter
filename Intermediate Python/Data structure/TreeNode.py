"""Cree una estructura de objetos que asemeje un Binary Tree.
- Debe incluir un método para hacer print de toda la estructura.
- No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections."""

#Represents a Node and what each attribute stores, self.data stores data, self.left and self.right points the child nodes.
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Pre-order, visits the root first, then the left subtree and then the right subtree, the arrow is printed before entering each child.
    def print_structure(self):
        print(self.data, end = "")
        if self.left is not None:
            print(" -> ", end = "")
            self.left.print_structure()
        if self.right is not None:
            print(" -> ", end = "")
            self.right.print_structure()


root = TreeNode("R")
#Left child of R
node_a = TreeNode("A")
#Right child of R
node_b = TreeNode("B")
#Left child of A
node_c = TreeNode("C")
#Right child of A
node_d = TreeNode("D")
#Left child of B
node_e = TreeNode("E")
#Right child of B
node_f = TreeNode("F")
#Left child of F
node_g = TreeNode("G")

#Root
root.left = node_a
root.right = node_b

#Left
node_a.left = node_c
node_a.right = node_d

#Right
node_b.left = node_e
node_b.right = node_f

#Child node
node_f.left = node_g

#Test
root.print_structure()