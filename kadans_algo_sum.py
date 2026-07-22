def check_kadans(arr):
    cur_sum = arr[0]
    max_sum = arr[0]
    
    for i in range(len(arr)):
        cur_sum = max(cur_sum+arr[i],arr[i])
        max_sum = max(cur_sum,max_sum)
        
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]

print(check_kadans(arr))