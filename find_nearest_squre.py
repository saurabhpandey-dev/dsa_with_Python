# def square(n):
#     if n<0:
#         print('invalid entry !!')
#         return
#     i=0
#     x=0
#     while i*i<=n:
#         if i*i == n:
#             x= i
#         i+=1
#     return float(i)
        

def square(n):
    low = 1
    high = n
    result=0
    
    while low<=high:
        mid = low+(high-low)//2
        
        if mid*mid == n:
            return mid
        
        if mid*mid <n:
            low = mid+1   
        else:
            high = mid-1
        
    return high

n = int(input('Enter the number : '))
print(square(n))
