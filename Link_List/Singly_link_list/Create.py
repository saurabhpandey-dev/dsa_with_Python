class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Single:
    def __init__(self,head=None):
        self.head = head
    
    def is_empty(self):
        return self.head is None
    
    def insert(self,data):
        newnode = Node(data)
        temp = self.head
        if self.is_empty():
            self.head = newnode
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode
                
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" -> ")
            temp = temp.next
        print('None')
        

n = Single()

n.insert(1)
n.insert(2)
n.insert(3)
n.insert(4)

n.display()

    
    
    
        