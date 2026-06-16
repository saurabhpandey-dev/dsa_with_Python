##QUS_10. Write a program to count the number of spaces in a string.

##def space_count(strings):
##    count =0
##    for string in strings:
##        if ' ' in string:
##            count+=1
##    return count
##
##
##name = input('Enter the string :- ')
##print(space_count(name))

name = input('Enter the string :- ')
print(name.count(' '))
