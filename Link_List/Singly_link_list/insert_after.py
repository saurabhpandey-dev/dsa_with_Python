class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class link:
    def __init__(self,head=None):
        self.head = head
        
    def is_empty(self):
        return self.head is None

    def insert(self,data):
        newnode = node(data)
        temp = self.head
        if self.is_empty():
            self.head = newnode
            return
        while(temp.next is not None):
            temp = temp.next
        
        temp.next = newnode
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end='->')
            temp = temp.next
            
    def ins_after(self,data,after):
        if self.head is None:
            print('List is Empty!')
            return
        temp = self.head
        newnode = node(data)
        while(temp.next is not None):
            if temp.data == after:
                newnode.next = temp.next
                temp.next = newnode
                return
            temp = temp.next
        print('position not found !!')
        
     
one = link()
one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)

one.traverse()   
print()
one.ins_after(25,20)
one.traverse()