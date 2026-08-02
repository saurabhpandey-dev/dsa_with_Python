# Iterable woh object hai jispe for loop chala sakte ho (jaise list, tuple, string)
#  — uske paas __iter__ method hoti hai. Iterator woh object hai jiske 
#  paas __next__ method hoti hai, jo ek-ek karke values deta hai aur khatam 
#  hone pe StopIteration raise karta hai. iter(iterable) call karke ek 
#  iterator milta hai.


lst = [1,2,3,4,5]

it = iter(lst)

print(next(it))  # 1
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # here the StopIteration exception becouse of no element left