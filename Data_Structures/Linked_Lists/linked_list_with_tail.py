class Linked_List_With_Tail:
    """ Python implementation of a linked list """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get_size(self):
        return self.size
        
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def get(self, index):
        if self.head:
            if index >= self.size or index < 0:
                print "Index is out of range"
                return
            elif index == 0:
                return self.front()
            elif index == self.size - 1:
                return self.back()
            else:
                node = self.head
                count = 0
                while count != index:
                    node = node.next_node
                    count += 1
                return node.value
        else:
            print "Cannot get value from an empty list"
            return
        
    def find(self, value):
        if self.head:
            node = self.head
            count = 0
            while node.value != value and count < self.size:
                node = node.next_node
                count += 1
                try:
                    node.value != value
                except:
                    return -1
            else:
                return count
        else:
            print "Cannot find value in an empty list"
            return
    
    def push_front(self, value):
        node = Node(value)
        if self.head:
            node.next_node = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        
    def pop_front(self):
        if self.head:
            node = self.head
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                self.head = None
                self.tail = None
            self.size -= 1
            del node
        else:
            print "Cannot remove element from an empty list"
            return
        
    def push_back(self, value):
        node = Node(value)
        self.tail.next_node = node
        self.tail = node
        self.size += 1
        
    def pop_back(self):
        if self.head:
            node = self.head
            while node.next_node != self.tail:
                node = node.next_node
            node.next_node = None
            del self.tail
            self.tail = node
            self.size -= 1
        else:
            print "Cannot remove value from an empty list"
            return
        
    def front(self):
        return self.head.value
        
    def back(self):
        return self.tail.value
        
    def insert(self, index, value):
        if self.head:
            if index >= self.size + 1 or index < 0:
                print "Index out of range"
                return
            elif index == 0:
                self.push_front(value)
            elif index == self.size:
                self.push_back(value)
            else:
                node = Node(value)
                cur_node = self.head
                count = 1
                while count != index:
                    cur_node = cur_node.next_node
                    count += 1
                temp_next = cur_node.next_node
                cur_node.next_node = node
                node.next_node = temp_next
                self.size += 1
                    
        elif index == 0:
            self.push_front(value)
        else:
            print "Index out of range (empty list)"
        
    def erase(self, index):
        if self.head:
            if index >= self.size or index < 0:
                print "Index is out of range"
                return
            elif index == 0:
                self.pop_front()
            elif index == self.size - 1:
                self.pop_back()
            else:
                cur_node = self.head
                count = 1
                while count != index:
                    cur_node = cur_node.next_node
                    count += 1
                temp_node = cur_node.next_node
                cur_node.next_node = temp_node.next_node
                del temp_node
                self.size -= 1
        else:
            print "Cannot remove value from an empty list"
            return
        
    def value_n_from_end(self, n):
        idx = self.size - n
        if idx < 0:
            print "Index out of range"
            return
        return self.get(idx)
        
    def reverse(self):
        if self.head:
            if self.size > 1:
                prev_node = self.head
                node = self.head.next_node
                self.tail = prev_node
                self.head = None
                prev_node.next_node = None
                while node.next_node:
                    temp_next = node.next_node
                    node.next_node = prev_node
                    prev_node = node
                    node = temp_next
                node.next_node = prev_node
                self.head = node
                    
        else:
            print "Cannot reverse an empty list"
            return
        
    def remove_value(self, value):
        idx = self.find(value)
        if idx == -1:
            print "Cannot remove value that isnt in list"
            return
        else:
            self.erase(idx)
    
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
        
