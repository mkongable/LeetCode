def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    # loop through s2 taking chunks the size of s1
    # if the chunk is a permutation of s1, return true
    # return false
    for i in range(len(s2) - len(s1) + 1):
        if self.isPermutation(s1, s2[i:i+len(s1)]):
            return True
    return False
def isPermutation(self, s1, s2):
    # if the lengths of s1 and s2 are not equal, return false
    if len(s1) != len(s2):
        return False
    # create a dictionary to keep track of the number of times each character appears in s1
    # iterate through s1
    # if the character is in the dictionary, increment the value by 1
    # otherwise, add the character to the dictionary with a value of 1
    # iterate through s2
    # if the character is in the dictionary, decrement the value by 1
    # otherwise, return false
    # iterate through the dictionary
    # if the value is not 0, return false
    # return true
    d = {}
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s2:
        if c in d:
            d[c] -= 1
        else:
            return False
    for c in d:
        if d[c] != 0:
            return False
    return True