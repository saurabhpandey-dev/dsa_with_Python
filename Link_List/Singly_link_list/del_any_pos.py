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

    def length(self):
        temp = self.head
        l=1
        while(temp.next is not None):
            l+=1
            temp = temp.next
        return l

    def del_pos(self,pos):
        temp = self.head
        if self.head is None:
            print('List is Empty!!')
            return
            
        if pos > self.length():
            print('Position out of Bound!')
            return
            
        if pos == 1:
            self.head = self.head.next
            return
        
        for _ in range(1,pos-1):
            temp = temp.next
        temp.next = temp.next.next
        
        
one = Link()

one.insert(10)
one.insert(20)
one.insert(30) 
one.insert(40)

one.traverse()
one.del_pos(2)
one.traverse()