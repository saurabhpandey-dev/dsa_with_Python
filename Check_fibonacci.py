a=0
b=1
n=int(input('enter the num'))

while(a<n):
    a,b = b,a+b

if a==n:
    print('yes')
else:
    print('no')
