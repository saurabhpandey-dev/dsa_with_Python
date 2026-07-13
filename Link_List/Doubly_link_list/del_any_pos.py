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
        temp = self.head
        if self.is_empty():
            self.head = newnode
            return
        while(temp.next is not None):
            temp=temp.next
        
        temp.next = newnode
        newnode.prev = temp
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=' <==> ')
            temp=temp.next 
        print(None,'\n') 
       
    def length(self):
        temp = self.head
        l=1
        while(temp.next is not None):
            l+=1
            temp = temp.next
        return l
      
    def del_pos(self,pos):
        if self.head is None:
            print('List is empty !!')
            return
        
        if pos > self.length():
            print('Position out of Bound.')
            return
        
        if pos == 1:
            self.head.prev = None
            self.head = self.head.next 
            return
        
        temp = self.head
        for _ in range(1,pos-1):
            temp = temp.next
        temp.next.prev = temp
        temp.next = temp.next.next
        
                
one=Link()
one.insert(1)
one.insert(2)
one.insert(3)
one.insert(4)
one.insert(5)

one.traverse()  

one.del_pos(4)
one.traverse()               
