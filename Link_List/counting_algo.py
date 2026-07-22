arr = [2,2,0,1,0,1]
count = [0,0,0]

for num in arr:
    count[num]+=1

index = 0
for value in range(3):
    for _ in range(count[value]):
        arr[index] = value
        index+=1
        
print(arr)