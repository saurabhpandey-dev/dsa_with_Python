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
        temp = self.head
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        while temp.next is not None:
            temp=temp.next
        newnode.prev = temp
        temp.next = newnode
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=' <==> ')
            temp = temp.next
        print(None,'\n')
    
    def ins_after(self,after,data):
              
        if self.head is None:
            print('List is Empty !!')
            return
        
        newnode = Node(data)
        
        if self.head.data == after:
            newnode.next = self.head.next
            self.head.prev = newnode
            self.head = newnode
            return 
        
        temp = self.head
        
        while temp.next is not None:
            if temp.data == after:
                newnode.next = temp.next
                newnode.prev = temp
                temp.next.prev = newnode
                temp.next = newnode
                return
            temp=temp.next
            
        newnode.prev = temp
        temp.next = newnode
            
one = Link()
one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)            

one.traverse()

one.ins_after(50,25)
one.traverse()