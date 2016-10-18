from queue_linked_list import Linked_List

class Queue(Linked_List):
    def enqueue(self, value):
        self.push_back(value)
    
    def dequeue(self):
        self.pop_front()
