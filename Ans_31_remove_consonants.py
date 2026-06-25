##QUS_31. Write a program to remove all consonants from a string while keeping vowels.


vowels = ['a','e','i','o','u']

string = 'saurabh ganguli pandey'

print(f'vowels : {vowels}')
print(f'String : {string}')

for s in string:
    if s not in vowels:
        string = string.replace(s,'')
    else:
        continue
    

print(string)
