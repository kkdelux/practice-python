# To solve hashing by chaining in Python I will need:
# -Linked List class (with a Node class) with methods:
#     * push_back(value)
#     * find(value)
#     * delete(value)
# -Hash function to map items to array as list nodes
# -Hash_Table data structure with the methods:
#     * add(key, value)
#     * exists(key)
#     * get(key)
#     * remove(key)

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def empty(self):
        if self.head:
            return False
        else:
            return True
    
    def push_back(self, key, value=None):
        node = Node(key, value)
        if self.tail:
            prev_tail = self.tail
            prev_tail.next_node = node
        else:
            self.head = node
        self.tail = node
        self.size += 1
        
    def find(self, key):
        if self.head:
            cur_node = self.head
            while cur_node:
                if cur_node.key and cur_node.key == key:
                    return cur_node
                else:
                    cur_node = cur_node.next_node
            return None
        else:
            return None
            
    def delete(self, key):
        if self.head:
            if self.head.key == key:
                node = self.head
                self.head = self.head.next_node
                del node
            elif self.head.key != key and self.head.next_node:
                prev_node = self.head
                node = self.head.next_node
                while node.key != key and node.next_node:
                    prev_node = node
                    node = node.next_node
                if node.key == key:
                    prev_node.next_node = node.next_node
                    if prev_node.next_node == None:
                        self.tail = prev_node
                else:
                    print "Cannot find key in list"
                    return
            else:
                print "Cannot find key in list"
                return
        else:
            print "Cannot delete element from empty list"
            return
        self.size -= 1
        
    def print_list(self):
        node = self.head
        while node:
            print (str(node.key) + " : " + str(node.value) + ", ") if node.value else (str(node.key) + ", "),
            node = node.next_node
        print
        
class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next_node = None
        
        
# Creating hash function outside hash table obj
def Hash(k, m):
    total = 0
    if type(k) is str:
        for i in k:
            total += ord(i)
    elif type(k) is int:
        total = k
    elif type(k) is float:
        total = int(k)
    return total % m
    
class Hash_Table:
    def __init__(self, size=8):
        self.table_size = size
        self.elem_size = 0
        self.arr = [Linked_List() for i in range(self.table_size)]
        
    def resize(self):
        if self.elem_size >= (self.table_size * 0.75):
            new_table = Hash_Table(self.table_size * 2)
            for i in self.arr:
                if not i.empty():
                    node = i.head
                    while node:
                        new_table.add(node.key[0], node.key[1])
                        node = node.next_node
            self = new_table
                        
        
    def add(self, key, value=None):
        self.resize()
        pos = Hash(key, self.table_size)
        if self.arr[pos].find(key):
            node = self.arr[pos].find(key)
            node.value = value
        else:
            self.arr[Hash(key, self.table_size)].push_back(key, value)
        self.elem_size += 1
        return
    
    def exists(self, key):
        pos = Hash(key, self.table_size)
        if self.arr[pos].find(key):
            return True
        else:
            return False
    
    def get(self, key):
        pos = Hash(key, self.table_size)
        node = self.arr[pos].find(key)
        if node:
            return node.value if node.value else node.key
        else:
            print "Key not found in table"
            return
    
    def remove(self, key):
        pos = Hash(key, self.table_size)
        node = self.arr[pos].find(key)
        if node:
            self.arr[pos].delete(node.key)
            return
        else:
            print "Cannot remove an unfound element from the table"
            return
    
    def print_table(self):
        for i in range(len(self.arr)):
            LL = self.arr[i]
            if not LL.empty():
                node = LL.head
                while node:
                    print (str(node.key) + " : " + str(node.value) + ", ") if node.value else (str(node.key) + ", "),
                    node = node.next_node
        print
        
HT = Hash_Table()
HT.add('kyle', 'strem')
HT.print_table()
HT.add(12)
HT.print_table()
print HT.exists(12)
print HT.get(12)
HT.remove('kyle')
HT.print_table()