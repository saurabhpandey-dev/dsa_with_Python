# here i find the program for find GCD 'Greatest Common Divisor'

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a= int(input('enter number 1 : '))
b= int(input('enter number 2 : '))

print(gcd(a,b))  
