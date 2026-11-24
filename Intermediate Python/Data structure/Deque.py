"""Cree una estructura de objetos que asemeje un Double Ended Queue.
- Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
- Debe incluir un método para hacer print de toda la estructura.
- No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections."""

#Basic structure to create nodes.
class Node:
    #Gives the code reader a clue of the data type used in the program
    data: str
    #Indicates that next must save another Node
    next: "Node"

    #Constructor
    def __init__(self, data, next = None, prev = None):
        #Saves the data in the node
        self.data = data
        #Saves the reference to the next node
        self.next = next
        #Saves the reference of the previous node
        self.prev = prev


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def push_right(self, data):
        #Creates a new node that holds the data
        new_node = Node(data)
        #Checks if the deque is empty
        if self.front is None:
            #Makes the new node both the first and the last one
            self.front = self.rear = new_node
        else:
            #Connects the current last node forward to the new one
            self.rear.next = new_node
            #Connects the new node backward to the previous last node
            new_node.prev = self.rear
            #Moves rear to the new node
            self.rear = new_node
        #Adds 1 to the counter
        self.size += 1


    def pop_left(self):
        #Checks if deque is empty and returns None if so
        if self.front is None:
            return None
        else:
            #Saves the node's data before moving it
            temporal_data = self.front.data
            #Moves front to the next node
            self.front = self.front.next
            #Checks if the deque is empty; if so, rear is set to None
            if self.front is None:
                self.rear = None
            #Removes the backward reference from the new first node, because nothing is in front of it anymore
            else:
                self.front.prev = None
            #Decreases the counter by 1
            self.size -= 1
            #Returns the data of the node that was removed
            return temporal_data


    def push_left(self, data):
        #Creates a new node that holds the data
        new_node = Node(data)
        #Checks if the deque is empty
        if self.front is None:
            self.front = self.rear = new_node
        else:
            #Connects the new node forward to the current first one
            new_node.next = self.front
            #Connects the current first node backward to the new one
            self.front.prev = new_node
            #Moves the front to the new node after the connections
            self.front = new_node
        #Adds 1 to the counter
        self.size += 1


    def pop_right(self):
        #Checks if deque is empty and returns None if so
        if self.front is None:
            return None
        else:
            #Saves the node's data before moving it
            removed_data = self.rear.data
            #Moves rear to the previous node
            self.rear = self.rear.prev
            #Checks if the deque is empty; if so, front is set to None
            if self.rear is None:
                self.front = None
            #Clears the forward connection of the new last node, because nothing comes after it anymore
            else:
                self.rear.next = None
        #Decreases the counter by 1
        self.size -= 1
        #Returns the data of the node that was removed
        return removed_data


    def print_structure(self):
        #Defines a variable that points to the front node
        current_node = self.front
        #Repeats the code while current_node holds a node; it stops when it reaches None
        while current_node:
            #Prints the data of the current node, and end="" prevents the line jump
            print(current_node.data, end="")
            #Ask if the current node has next, and if it is None means that's the last node
            if current_node.next is not None:
                #Prints the arrow without the line jump only if there's a node after
                print(" -> ", end="")
            #Advance to the next node, so the next while turn works with that node
            current_node = current_node.next
        print()


d = Deque()
d.print_structure()
#Push right
d.push_right("A")
d.push_right("B")
d.push_right("C")
d.print_structure()
#Push left
d.push_left("Z")
d.print_structure()
#Pop left
d.pop_left()
#Pop right
d.pop_right()
d.print_structure()