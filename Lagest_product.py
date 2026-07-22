
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num = int(input('enter the num : '))
lst = [a for a in range(1,num) if gcd(num,a)==1]

mul=1
for i in lst:
    mul = mul*i

print(lst)
print(mul%num)

for i in range(num):
    if sum
    
    
    