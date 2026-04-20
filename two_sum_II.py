#expects an sorted array

class Solution:
    def twoSumTwo(numbers, sum):
        n = len(numbers)
        l, r = 0, n - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum == sum:
                return [l, r]
            elif curSum > sum:
                r -= 1
            else: 
                l += 1
        
        return False
   
    
arr = [2, 7, 11, 15]
twoSumClass = Solution() 
print(Solution.twoSumTwo(arr, 26))
                
            
