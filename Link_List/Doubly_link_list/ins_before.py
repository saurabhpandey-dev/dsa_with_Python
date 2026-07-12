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
    
    def length(self):
        temp = self.head
        l=1
        while(temp.next is not None):
            l+=1
            temp = temp.next
        return l 
    
    def ins_before(self,data,before=None):
        if self.head == None:
            print('List is empty !!')
            return
        newnode = Node(data)
        temp = self.head
        
        if before==None:
            while temp.next is not None:
                temp=temp.next
            temp.next = newnode
            newnode.prev=temp
            
        if self.head.data == before:
            newnode.next = self.head
            self.head.next.prev = newnode
            self.head=newnode
            return
        while temp.next is not None:
            if temp.next.data == before:
                newnode.next = temp.next 
                newnode.prev = temp
                temp.next.prev = newnode
                temp.next = newnode
                return
            temp=temp.next
                   
    
one = Link()
one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)            

one.traverse()

one.ins_before(25,40)
one.traverse()