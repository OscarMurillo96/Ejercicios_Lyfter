"""Cree una estructura de objetos que asemeje un Stack.
- Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
- Debe incluir un método para hacer print de toda la estructura.
- No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections."""


#Basic structure to create nodes.
class Node:
    #Gives the code reader a clue of the data type used in the program
    data: str
    #Indicates that next must save another Node
    next: "Node"

    #Constructor
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#Defines a Stack class
class Stack:
    #Type annotation that indicates that head can save a Node or a None value when it is empty.
    head: Node

    #Initialization of the head attribute of the Stack
    def __init__(self, head = None):
        self.head = head

    #Method to push into the Stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Returns the data of the Node that was popped
    def pop(self):
        if self.isEmpty():
            return "Stack is empty!"
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    #Verifies if the Stack is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    #Prints the Stack in a LIFO structure
    def print_structure(self):
        #Defines a variable that points to the head node
        current_node = self.head
        #Repeats the code while current_node holds a node; it stops when it reaches None
        while current_node:
            #Prints the data of the current node, and end="" prevents the line jump
            print(current_node.data, end="")
            #Ask if the current node has next, and if it is None means that's the last node
            if not current_node.next == None:
                #Prints the arrow without the line jump only if there's a node after
                print(" -> ", end="")
            #Advance to the next node, so the next while turn works with that node
            current_node = current_node.next
        print()


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.print_structure()
s.pop()
s.print_structure()

#Testing an empty Stack scenario
s = Stack()
print(s.pop())
s.print_structure()