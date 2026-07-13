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
    
    def get_pos(self,data):
        if self.head is None:
            print('list is empaty !!')            
            return
        if self.head.data == data:
            return 1
        temp = self.head
        l=1
        while(temp.next is not None):
            l+=1
            temp = temp.next
            if temp.data == data:
                return l
     
    def search(self,data):
        if self.head is None:
            print('List is empty')
            return
        
        temp = self.head   
        while temp is not None:
            if temp.data == data:
                print(f'Node {data} found\n')
                print(f'Node position : {self.get_pos(data)}')
                return
            temp = temp.next
        print('Node not Found!!')
        
one=Link()
one.insert(1)
one.insert(2)
one.insert(3)
one.insert(4)
one.insert(5)

one.traverse()                 
one.search(1)