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
       
    def del_specific_val(self,data):
        if self.head is None:
            print('list is empty !!')
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next is not None:
            if temp.next.data == data:
                temp.next.next.prev=temp
                temp.next = temp.next.next
                return
            temp = temp.next 
        print('data not found!!')
        
one=Link()
one.insert(1)
one.insert(2)
one.insert(3)
one.insert(4)
one.insert(5)

one.traverse()  

one.del_specific_val(4)
one.traverse()               