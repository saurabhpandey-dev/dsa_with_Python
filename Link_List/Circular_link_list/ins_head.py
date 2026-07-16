class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 
        
class Link:
    def __init__(self,tail=None):
        self.tail = tail
        
    def insert(self,data):
        newnode = Node(data)
        if self.tail is None:
            newnode.next = newnode
            self.tail = newnode
            return      
        newnode.next = self.tail.next
        self.tail.next = newnode
        self.tail = newnode
        
    def traverse(self):
        temp = self.tail.next
        while temp != self.tail:
            print(temp.data,end=' -> ')
            temp = temp.next
        print(temp.data,' -> ',None,'\n')

    def ins_head(self,data):
        if self.tail is None:
            print('List is Empty')
            return
        temp = self.tail.next 
        newnode = Node(data)
        newnode.next = temp
        self.tail.next = newnode
  
  
one = Link()

one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)

one.traverse()     

one.ins_head(5)
one.traverse() 