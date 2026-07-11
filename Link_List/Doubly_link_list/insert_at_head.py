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
            temp=temp.next
        
        temp.next = newnode
        newnode.prev = temp.next
        
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=' -> ')
            temp = temp.next
        print(None)
        
    def ins_start(self,data):
        newnode = Node(data)
        if self.is_empty():
            self.head = newnode
            return
        
        temp = self.head
        newnode.next = self.head
        temp.prev = newnode
        self.head = newnode
    
one=Link()
one.insert(1)
one.insert(2)
one.insert(3)
one.insert(4)
one.insert(5)

one.traverse()                 

one.ins_start(0.5)
one.traverse()