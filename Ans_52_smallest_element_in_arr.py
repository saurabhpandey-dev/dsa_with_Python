arr = [4,8,4,3,4,9,4,7,2]

# here i use sort function for sort the array and return the first element
# arr.sort()
# print(arr[0])

# here use min() for find the smallest element
# print(min(arr))

# here is a normal program
n=arr[0]
for num in arr:
    if num<n:
        n=num

print(n)