def check_max(arr,k):
    if len(arr)<k:
        return

    cur_sum = sum(arr[:k])
    max_sum = cur_sum
    
    for i in range(k,len(arr)):
        cur_sum += cur_sum + arr[i] - arr[i-k]
        max_sum = max(cur_sum,max_sum)

    return max_sum

arr = [2,1,5,1,2,3]
k=3
print(check_max(arr,k))