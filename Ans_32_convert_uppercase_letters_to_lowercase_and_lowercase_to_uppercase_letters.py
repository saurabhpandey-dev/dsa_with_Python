##QUS_32. Write a program to convert uppercase letters to lowercase and lowercase letters
##to uppercase.


string = 'SauraBh GanGuli PanDey'

i=0
while i<=len(string):
    if string[i].isupper():
        string[i] = string[i].lower()
    else:
        pass

print(string)
