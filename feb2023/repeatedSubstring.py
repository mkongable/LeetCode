def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # loop thru the string
    # break into evenly divisible substrings
    # check if the substring is repeated
    for i in range(1, len(s)//2 + 1):
        if len(s) % i == 0:
            if s[:i] * (len(s)//i) == s:
                return True
    return False