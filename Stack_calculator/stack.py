from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            old_top = self.top
            self.top = self.top.next
            old_top.next = None
            self.size -= 1
            return old_top.data
