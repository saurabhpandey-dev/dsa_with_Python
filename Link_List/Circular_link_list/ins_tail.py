class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
class Link:
    def __init__(self,tail=None):
        self.tail=tail 
    
    def insert(self,data):
        newnode = Node(data)
        if self.tail is None:
            self.tail = newnode
            newnode.next = newnode
            return
        newnode.next = self.tail.next 
        self.tail.next = newnode 
        self.tail = newnode
        
    def traverse(self):
        temp = self.tail.next
        while temp is not self.tail:
            print(temp.data,end=' -> ')        
            temp = temp.next 
        print(temp.data,'->',None,'\n')
    
    def ins_last(self,data):
        if self.tail is None:
            print('list is empty!!')
            return
        
        temp = self.tail 
        newnode = Node(data)
        newnode.next = self.tail.next 
        self.tail.next = newnode
        self.tail = newnode
        print('data insert into the last\n')
        
one = Link()
one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)

one.traverse()
one.ins_last(60)
one.traverse()