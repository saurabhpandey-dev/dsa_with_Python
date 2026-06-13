#Qus 5. Write a program to reverse a given string and display the result.

str = 'hello world'
reversed_s1 = str[::-1]
print(f' first way to convert {reversed_s1}')

reversed_s2 = "".join(reversed(str))
print(f' second way to convert {reversed_s2}')

