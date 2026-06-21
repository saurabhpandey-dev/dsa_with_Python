##Qus_18. Write a program to remove all spaces from a string.

string = '  ich bin Saurabh!    '

##string = string.strip(' ')# it only replace left and right space on string
string = string.replace(" ","")  # here i replace all space
print(string,end=".")
