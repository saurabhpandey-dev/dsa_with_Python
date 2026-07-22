class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Link:
    def __init__(self,head=None):
        self.head = head
    
    def is_empty(self):
        return self.head is None
    
    def insert(self,data):
        newnode = Node(data)
        temp = self.head
        if self.is_empty():
            self.head = newnode
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
                
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" -> ")
            temp = temp.next
        print('None')
    
    def concate(self,two):
        temp=self.head
        while temp is not None:
            print(temp.data,end=' -> ')
            temp=temp.next 
            if temp.next == None:
                temp = two.head
            
    
one = Link()

one.insert(1)
one.insert(2)
one.insert(3)
one.insert(4)
one.traverse()

two = Link()

two.insert(5)
two.insert(6)
two.insert(7)
two.insert(8)
two.traverse()  
    
one.concate(two)

one.traverse()
        