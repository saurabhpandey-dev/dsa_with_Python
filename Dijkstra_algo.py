lst = [4,5,6,4,5]

low = 0
mid = 0
high = len(lst)-1

while mid<=high:
    if lst[mid] == 4:
        lst[low],lst[mid]=lst[mid],lst[low]
        low = low + 1
        mid = mid + 1
    elif lst[mid] == 5:
        mid = mid + 1
    elif lst[mid] == 6:
        lst[mid],lst[high] = lst[high],lst[mid]
        high = high-1

print(lst)