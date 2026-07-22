arr = [2,2,3,3,3,1,2,3]
count = 0 
candidate = 0

for i in range(len(arr)):
    x =arr[i]
    if count == 0:
        count += 1
        candidate = x
    if x == candidate:
        count+=1
    else:
        count-=1
    
    for i in range(len(arr)):
        if candidate == arr[i]:
            count+=1

    count = 0
    for i in range(len(arr)):
        if candidate == arr[i]:
            count+=1
        a = arr.len()
        if count> a/2:
            print('mejority')
        else:
            print('no')