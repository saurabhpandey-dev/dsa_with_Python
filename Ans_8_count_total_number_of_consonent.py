##QUS_8. Write a program to count the total number of consonants in a string.


def check_vowels(strings):
    vowels = ['a','e','i','o','u']
    count =0
    for char in strings:
        if not char in vowels:
            count+=1
    return count

strings = input('enter the String :- ')
print(check_vowels(strings))
