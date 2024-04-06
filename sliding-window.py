def lengthOfLongestSubstring(s):
    state = {}
    longest = 0
    start = 0

    for end in range(len(s)):
        currChar = s[end]
        if currChar in state:
            count = state[currChar] + 1
        else:
            count = 1
        
        #update state
        state[currChar] = count

        #shrinking window if necesseary
        while state[currChar] > 1:
            prevCount = state[s[start]]
            state[s[start]] = prevCount - 1
            start += 1
        
        longest = max(end - start + 1, longest)
    
    return longest

print(lengthOfLongestSubstring('kwbbpep'))