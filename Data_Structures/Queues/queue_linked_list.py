class Linked_List:
    """ Python implementation of a linked list to be used with queues """
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push_back(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next_node = node
        else:
            self.head = node
        self.tail = node
        
    def pop_front(self):
        if self.head:
            node = self.head
            if node.next_node:
                self.head = node.next_node
            else:
                self.head = None
                self.tail = None
            del node
        else:
            print "Cannot remove element from an empty list"
            return
        
    def empty(self):
        if self.head:
            return False
        else:
            return True
            
    def print_list(self):
        node = self.head
        while node:
            print node.value,
            node = node.next_node
        print
            
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None