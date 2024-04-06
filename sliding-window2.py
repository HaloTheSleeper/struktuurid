def maxLengthOfSubstring(s):
    state = {}
    longest = start = 0

    for end in range(len(s)):
        currChar = s[end]

        if currChar in state:
            state[currChar] = state[currChar] + 1
        else:
            state[currChar] = 1

        while state[currChar] > 1:
            state[s[start]] = state[s[start]] - 1
            start += 1

        longest = max(end - start + 1, longest)

    return longest

print(maxLengthOfSubstring('kwbbgepis'))


