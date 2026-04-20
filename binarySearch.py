def binarySearch(arr, target):
    l = 0 
    r = len(arr)
    m = (l + r) // 2
    
    
    while l <= r: 
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m
            m = (l + r) // 2
        else:
            r = m
            m = (l + r) // 2
    
    return -1
        


arr = [2, 3, 4, 10, 40]
x = 10

print(binarySearch(arr, x))
   