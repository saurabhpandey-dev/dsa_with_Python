##Qus7. Write a program to count the total number of vowels in a string.

##def check_vowels(strings):
##    vowels = ['a','e','i','o','u']
##    count =0
##    for string in strings:
##       for vowel in vowels:
##          if string == vowel:
##             count+=1
##          else:
##             pass
##    return count

def check_vowels(strings):
    vowels = ['a','e','i','o','u']
    count =0
    for char in strings:
        if char in vowels:
            count+=1
    return count

strings = input('enter the String :- ')
print(check_vowels(strings))
