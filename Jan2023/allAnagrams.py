def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    # make a dictionary to keep track of the number of times each character appears in p
    # loop through s taking chunks the size of p
    # using the sliding window method
        # as you move the window, add the character at the end of the window to the dictionary and remove the character at the beginning
        # if the dictionary is equal to the dictionary of p, add the index of the beginning of the window to the list
    # return the list
    d = {}
    for c in p:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    l = []
    for i in range(len(s) - len(p) + 1): # loop through s taking chunks the size of p
        if i == 0:
            d2 = {}
            for c in s[i:i+len(p)]: # loop through the chunk
                if c in d2: # if the character is in the dictionary, increment the value by 1
                    d2[c] += 1 
                else:
                    d2[c] = 1
        else:
            #remove character at the beginning of the window
            # if greater than 1, decrement the value by 1
            # if equal to 1, remove the key
            if d2[s[i-1]] > 1:
                d2[s[i-1]] -= 1
            else:
                d2.pop(s[i-1])
            if s[i+len(p)-1] in d2: 
                d2[s[i+len(p)-1]] += 1 # add the character at the end of the window to the dictionary
            else:
                d2[s[i+len(p)-1]] = 1 
        if d == d2:
            l.append(i)
    return l

s = "cbaebabacd"
p = "abc"
print(findAnagrams(any, s, p))
