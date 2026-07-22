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
    
    def duplicate(self):
        temp1= self.head
        while temp1 is not None:
            temp2 = temp1 
            while temp2 is not None:
                if temp1.data == temp2.data:
                    temp1.next = temp2.next
                temp2 = temp2.next
            temp1=temp1.next
                
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
n.insert(5)
n.insert(3)

n.display()

n.duplicate()
n.display()
    
    
        

# temp1= head
#         while temp1 is not None:
#             temp2 = temp1 
#             while temp2 is not None:
#                 if temp1.data == temp2.data:
#                     temp1.next = temp2.next
#                 temp2 = temp2.next
#             temp1=temp1.next
#         return head
    
    
    
    
# res = head

#         while head and head.next:
#             if head.data == head.next.data:
#                 head.next = head.next.next
#             else:
#                 head = head.next
        
#         return res