# Generator ek special function hai jo 'return' ki jagah 'yield' use karti
# hai. Jab call hoti hai to yeh function turant nahi chalta — ek generator
# object return hota hai, aur code sirf tab-tab chalta hai jab next() call
# hoti hai. Isse pura data ek saath memory me store nahi karna
# padta — bahut memory-efficient hota hai large data ke liye.

def count_no(n):
    i = 1
    while i <= n:
        yield i 
        i= i+1
    
gen = count_no(8)
print(next(gen))  # 1
print(next(gen))  # 2
for val in gen:
    print(val)      # 3 (resume from where it stopped)
