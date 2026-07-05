class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class link:
    def __init__(self,head=None):
        self.head = head
    
    def is_empty(self):
        return self.head is None
    
    def insert(self, data):
        newnode = node(data)
        temp = self.head
        
        if self.is_empty():
            self.head = newnode
            return
        
        while(temp.next is not None):
            temp = temp.next
        temp.next = newnode
    
    def ins_pos(self,data,pos):
        temp = self.head
        newnode = node(data)
        i=1
        while(i<pos-1):
            i+=1
            temp = temp.next
            
        newnode.next = temp.next
        temp.next = newnode        
                
    def traverse(self):
        temp =  self.head
        while(temp is not None):
            print(temp.data)
            temp = temp.next
    
    
one = link()

one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)

one.traverse()
print()
one.ins_pos(35,3)
one.traverse()