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
            
    def ins_before(self,data,before):
        
        temp = self.head
        newnode = node(data)
        if self.head is None:
            print('list is empty !!')
            return

        if self.head.data == before:
            newnode.next = self.head
            self.head = newnode
            return
        
        while temp.next is not None:
            if temp.next.data == before:
                newnode.next = temp.next
                temp.next = newnode                
                return
            temp = temp.next
        print(f"Node '{before}' not found in the list.")

    def ins_before2(self,data,before): 
        temp = self.head
        newnode = node(data)
        loc = self.get_pos(before)
        if loc == 1:
            newnode.next = head
            self.head = newnode
            return                   
        i=1
        while(temp is not None and i<loc-1):
            temp=temp.next
            i+=1
        newnode.next = temp.next
        temp.next = newnode
        
                           
    def get_pos(self,data):
        if self.head is None:
            print('list is empaty !!')            
            return
        temp = self.head
        l=1
        while(temp.next is not None):
            l+=1
            temp = temp.next
            if temp.data == data:
                return l
    
one = link()
one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)

one.traverse()   
print()
# one.ins_before(25,20)
one.ins_before2(25,20)
one.traverse()
print()
print(one.get_pos(20))