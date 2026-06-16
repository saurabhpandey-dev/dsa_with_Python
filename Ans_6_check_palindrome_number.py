##QUS 6. Write a program to check whether a given string is a palindrome or not.

def palindrome (s):
    return str(s)== str(s)[::-1]



x = int(input('Enter the number :- '))
print(palindrome(x))
