# String immutable kyun hai, aur iska practical impact kya hai?
# String immutable design decision hai — memory efficiency aur hashability 
# (dict keys, set elements ban sakte hain) ke liye. Practical impact yeh hai 
# ki jab tum string ko 'modify' karte lagte ho, actually har baar naya string 
# object banta hai.


s = 'Saurabh'
id1 = id(s)

s = s + ' Pandey'

id2 = id(s)

print(id1)
print(id2)
print(id1 == id2)