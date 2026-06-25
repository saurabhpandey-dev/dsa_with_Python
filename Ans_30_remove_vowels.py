##QUS_30. Write a program to from a string.


vowels = ['a','e','i','o','u']

string = 'saurabh ganguli pandey'

print(f'vowels : {vowels}')
print(f'String : {string}')

for s in string:
    if s not in vowels:
        continue
    else:
        string = string.replace(s,'')
    

print(string)
