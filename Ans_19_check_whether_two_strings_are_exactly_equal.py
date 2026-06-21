##Qus_19. Write a program to check whether two strings are exactly equal.

string1 = 'saurabh'
string2 = 'surabh'

print('method one')

if string1 == string2:
    print("both are same content's")
else:
    print('not same yet!')

    
print('method two')

if string1.__eq__(string2):
    print("both are same content's")
else:
    print('not same yet!')
