#find if array has consecutive numbers that add up to a specific number
def canWeMakeItMatch(arr, n):
    if len(arr) < 1:
        return False
    
    start = sumOfNumbers = 0

    for end in range(len(arr)):
        sumOfNumbers += arr[end]

        while sumOfNumbers > n:
            sumOfNumbers -= arr[start]
            start += 1
        
        if sumOfNumbers == n:
            return True
        
    return False




arr = [3, 4, 1, 8, 2]
print(canWeMakeItMatch(arr, 13))
