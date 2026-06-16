##QUS_11. Write a program to count the number of special characters in a string.

name = '@#saurabh*('

count=0
for n in name:
    if n.isalnum() == True:
        count+=1

print(count)
