# lst = [4,6,10,7,5,9,3]

# here i use normal brout force program
# n=lst[0]

# for num in lst:
#     if num >  n:
#         n=num  
# print(n)


#here i sort the list and return the last element
# lst.sort()
# print(lst[-1])


#here i use max fun for find max
# print(max(lst))


num = input('enter the number of list : ')

lst = list(num.split())

count = 0
for i in lst:
    count = count + 1

for i in range(count):
    lst[i] = int(lst[i])

n = lst[0]
for num in lst:
    if num > n :
        n = num

print(n)