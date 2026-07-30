# String concatenation loop me '+' use karna bad practice kyun mana jaata hai?
# Kyunki string immutable hai, har '+' operation naya string object banata 
# hai — loop me n baar concatenation O(n^2) time le sakta hai.
# Behtar tareeka hai ''.join(list) use karna, jo O(n) me kaam karta hai.

words = ['Saurabh ','Ganguli ','Pandey']
result = ''
# for word in words:
#     result += word  # here time is O(n^2)


result = ''.join(words) # it use O(n) time 
print(result)

