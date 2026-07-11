class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next
    
class Link:
    def __init__(self,head=None):
        self.head = head
    
    def is_empty(self):
        return self.head is None
    
    def insert(self,data):
        newnode = Node(data)
        temp=self.head
        if self.is_empty():
            self.head = newnode
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode