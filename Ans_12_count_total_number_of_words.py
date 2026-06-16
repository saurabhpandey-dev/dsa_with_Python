##QUS_12. Write a program to count the total number of words in a sentence.

def count_word(string):
    lst = list(string.split())
    return len(lst)

text = input("enter the string :-")
print(count_word(text))


##text = "I am the God!"
##word_count = len(text.split())
##print(word_count)  
