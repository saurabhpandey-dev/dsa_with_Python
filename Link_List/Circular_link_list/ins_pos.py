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
            self.tail = newnode
            newnode.next = newnode
            return
        newnode.next = self.tail.next 
        self.tail.next = newnode
        self.tail = newnode
    
    def traverse(self):
        temp = self.tail.next
        while(temp is not self.tail):
            print(temp.data,end=' -> ')
            temp = temp.next
        print(temp.data,' -> ',None)

    def length(self):
        if self.tail is None:
            print('list is empty !!')
            return
        count = 1
        temp = self.tail.next 
        while(temp is not self.tail):
            count = count+1
            temp = temp.next 
        return count
        
    def ins_pos(self,pos,data):
        if self.tail is None:
            print('list is empty !!')
            return
        
        if pos >= self.length()+2:
            print('List out of bound!!')
            return
        
        newnode = Node(data)
        if pos == 1:
            newnode.next = self.tail.next
            self.tail.next = newnode
            return
        
        if pos == self.length()+1:
            newnode.next = self.tail.next 
            self.tail.next = newnode
            self.tail = newnode
            return 
        
        temp = self.tail.next 
        i=1
        while temp is not self.tail:
            if i == pos - 1:
                newnode.next = temp.next 
                temp.next = newnode
                return
            i=i+1
            temp = temp.next 

    
one = Link()

one.insert(10)
one.insert(20)
one.insert(30)
one.insert(40)
one.insert(50)        
        
one.traverse()
# print(one.length())
one.ins_pos(6,25)
one.traverse()
            