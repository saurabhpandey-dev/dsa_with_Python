def check_kadans(arr):
    cur_sum = arr[0]
    max_sum = arr[0]
    start = 0
    end = 0
    for i in range(len(arr)):
        cur_sum = max(cur_sum+arr[i],arr[i])
        max_sum = max(cur_sum,max_sum)
        
        if arr[i] > arr[i]+cur_sum:
            tempstart = i
            
        if (cur_sum >max_sum):
            max_sum = cur_sum
            start = tempstart
            end = i

    print(arr[start:end])
    
arr = [-2,1,-3,4,-1,2,1,-5,4]

check_kadans(arr)