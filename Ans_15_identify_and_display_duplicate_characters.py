##QUS_15. Write a program to identify and display duplicate characters in a string.

def dupli(name):
    lst = []
    for x in name:
        a= name.count(x)
        lst.append([x,a])
    return lst


name = 'kamla pasand'
print(dupli(name))

