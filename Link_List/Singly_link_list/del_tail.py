class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class Link:
    def __init__(self,head=None):
        self.head = head
    
    def insert(self,data=0):
        temp = self.head
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        while(temp.next is not None):
            temp = temp.next 
        temp.next = newnode
        
    def traverse(self):
            temp = self.head
            while temp is not None:
                print(temp.data,end=' -> ')
                temp =temp.next 
            print(None,'\n')
   
    def del_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next 
        temp.next = None    
    
one = Link()

one.insert(10)
one.insert(20)
one.insert(30) 
one.insert(40)

one.traverse()
one.del_tail()
one.traverse()