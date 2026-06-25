##QUS_27. Write a program to extract a substring from a given string using specified start
##and end positions.

string = 'saurabh'
def extract(start,end):
    return string[start:end]

print(string)
start = int(input('Start from ? :'))
ends = int(input('Ends where ? :'))
print(extract(start,ends))
