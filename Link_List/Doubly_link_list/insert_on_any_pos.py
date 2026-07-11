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
            print(temp.data,end=' -> ')
            temp = temp.next
        print(None)
    
    def length(self):
        temp = self.head
        l=1
        while(temp.next is not None):
            l+=1
            temp = temp.next
        return l 
    
    def ins_pos(self,pos,data):
        temp = self.head
        if self.head is None:
            print('list is Empty !!')
            return
        newnode = Node(data)

        if pos == 1:
            newnode.next = self.head
            newnode.next.prev = newnode
            self.head = newnode
            return

        if pos-1 == self.length():
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
            return
        
        if pos > self.length():
            print('position out of bound !')
            return
                          
        i=1
        while i<pos-1:
            temp = temp.next 
            i+=1
        newnode.prev = temp
        newnode.next = temp.next
        temp.next.prev = newnode
        temp.next = newnode
        
        
one = Link()
one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)            

one.traverse()
print()
one.ins_pos(2,25)
one.traverse()
print()
one.ins_pos(7,3)
one.traverse()