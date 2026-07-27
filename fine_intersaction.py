class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next 

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
        print(None)

    def marge(self,list2,target_data):
        if self.is_empty() or list2.is_empty():
            print('any list is empty!')
            return
          
        intersaction = None
        
        temp= self.head
        while(temp.next is not None):
            if temp.data == target_data:
                intersaction = temp
                break
            temp=temp.next
           
        if intersaction == None:
            print(f'target data {target_data} not found !')
            return
        
        temp2 = list2.head
        while(temp2.next is not None):
            temp2 = temp2.next
            
        temp2.next = intersaction
        
        
    def check_intersaction(self,head2):
        temp1 = self.head
        temp2 = head2.head
        
        if not temp1 is not temp2:
            print('any one list is empty !!')
            return
        
        while(temp1 is not temp2):
                        
            if temp1 is None:
                temp1 = head2.head
            else:
                temp1 = temp1.next
                
            if temp2 is None:
                temp2 = self.head
            else:
                temp2 = temp2.next
         
        if temp1 is not None:
            print('list 1 and list 2 have intersaction')
        else:
            print('list 1 and list 2 have no intersaction')
                  
          
# one = link()
# one.insert(1)
# one.insert(2)
# one.insert(3)
# one.insert(7)
# one.insert(8)
# one.insert(9)

# two = link()
# two.insert(8)
# two.insert(6)

one = link()
one.insert(1)
one.insert(2)
one.insert(3)
one.insert(7)

two = link()
two.insert(4)
two.insert(5)
two.insert(6)

one.traverse()
print()
two.traverse()
print('\n')
one.marge(two,7)

print('\n\nafter marge : \n')
one.traverse()
two.traverse()
print('\n')

one.check_intersaction(two)