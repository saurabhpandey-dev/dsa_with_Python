#program to calculate the avgrage height from a list of height 

heights = input('Enter the numbers')

lst = heights.split(' ')

# this not work becouse height is str and str is not do any sliceing only number
# for height in lst:
#     lst[height] = int(lst[height])
#     print(type(height))

print(lst) # here is a all value is str

count = 0
for height in lst: # here find total number of element in list
    count += 1

# print(count)

i = 0
for i in range(count):  
    lst[i] = int(lst[i]) # here convert str element to int element of whole list

print(lst) # here is a all value is int

total =0
for j in range(count):
    total = total + lst[j]

avg_height = round(total/(i+1)) # here calculate the average height os list

print(avg_height) # here print the average height
