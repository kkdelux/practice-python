class Linked_List:
    """ Python implementation of a linked list """
    def __init__(self):
        self.head = None
        self.size = 0
        
    def get_size(self):
        return self.size
        
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def get(self, index):
        if index > self.size - 1 or index < 0:
            return "Index out of range"
        else:
            count = 0
            node = self.head
            while count != index:
                node = node.next_node
                count += 1
            return node.value
        
    def find(self, value):
        if self.size > 0:
            count = 0
            node = self.head
            cur_val = node.value
            while cur_val != value and count < self.size:
                node = node.next_node
                cur_val = node.value
                count += 1
            if count == self.size:
                return -1
            else:
                return count
        else:
            return "Cannot find value in an empty list"
    
    def push_front(self, value):
        node = Node(value)
        if self.head:
            node.next_node = self.head
            self.head = node
        else:
            self.head = node
        self.size += 1
        
    def pop_front(self):
        node = self.head
        if self.head.next_node:
            self.head = self.head.next_node
        else:
            self.head = None
        self.size -= 1
        del node
        
    def push_back(self, value):
        node = Node(value)
        cur_node = self.head
        while cur_node.next_node:
            cur_node = cur_node.next_node
        cur_node.next_node = node
        self.size += 1
        
    def pop_back(self):
        if self.head:
            if not self.head.next_node:
                node = self.head
                self.head = None
                del node
            else:
                node = self.head.next_node
                prev_node = self.head
                while node.next_node:
                    prev_node = node
                    node = node.next_node
                del node
                prev_node.next_node = None
            self.size -= 1
        else:
            return "No back value in an empty list"
        
    def front(self):
        if self.head:
            return self.head.value
        else:
            return "No front value in an empty list"
        
    def back(self):
        if self.head:
            node = self.head
            while node.next_node:
                node = node.next_node
            return node.value
        else:
            return "No back value in an empty list"
        
    def insert(self, index, value):
        if self.size > 0 and (index < self.size and index > 0):
            node = Node(value)
            cur_node = self.head
            count = 0
            while count != index - 1:
                count += 1
                cur_node = cur_node.next_node
            temp_next = cur_node.next_node
            cur_node.next_node = node
            node.next_node = temp_next
            self.size += 1
            
        elif index == 0:
            self.push_front(value)
            self.size += 1
            
        elif index >= self.size or index < 0:
            print "Index out of range"
            return
        
        else:
            print "List is empty, try obj.push_front or obj.push_back"
            return
        
    def erase(self, index):
        if self.size > 0:
            if self.size > 1 and (index > 0 and index < self.size):
                prev_node = self.head
                node = prev_node.next_node
                count = 1
                while count != index:
                    prev_node = prev_node.next_node
                    node = node.next_node
                    count += 1
                prev_node.next_node = node.next_node
                del node
                self.size -= 1
                
            elif index == 0:
                self.pop_front()
                self.size -= 1
            else:
                print "Index is out of range"
        else:
            print "Cannot erase element from an empty list"
        
    def value_n_from_end(self, n):
        forward_n = self.size - n
        if forward_n < 0:
            print "Index out of range"
            return
        return self.get(forward_n)
        
        
    def reverse(self):
        if self.size > 1:
            prev_node = self.head
            node = self.head.next_node
            self.head = None
            prev_node.next_node = None
            while node.next_node:
                temp_next = node.next_node
                node.next_node = prev_node
                prev_node = node
                node = temp_next
            node.next_node = prev_node
            self.head = node
        
    def remove_value(self, value):
        self.erase(self.find(value))
    
    def print_list(self):
        node = self.head
        while node:
            print node.value,
            node = node.next_node
        print
        
    
    
    
class Node:
    """ Node for each link of the linked list """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        

