class Solution:
    def strStr(self, haystack, needle):
        if needle == "": return 0
        
        lps = [0] * len(needle)
        
        i, prevLps = 1, 0
        while i < len(needle):
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                i, prevLps = i + 1, prevLps + 1
            elif prevLps == 0:
                i += 1
            else: 
                prevLps = lps[prevLps - 1]
        
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]
            
            if (j == len(needle)): 
                return i - len(needle)
        
        return -1

solution = Solution()
print(solution.strStr("AAAABA", "AAABA"))
        