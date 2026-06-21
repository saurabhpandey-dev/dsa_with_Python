##QUS_16. Write a program to remove duplicate characters from a string while
##keeping the first occurrence.

string = 'bottol'
lst=[]

##i=1
##lst.append(string[0])
##while i<=len(string)-1:
##    if string[i] in lst:
##        i+=1
##        continue
##    lst.append(string[i])
##    i+=1
##print(lst)

for char in string:
    if char not in lst:
        lst.append(char)

print(lst)
