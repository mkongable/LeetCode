def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    # take slices of str1 starting from the beginning and see if they are a GCD
    # take the biggest GCD after evaluating all of them (every slice possible with str1 that starts at the beginning)
    # if there is no GCD, return ""
    biggestGCD = ""
    for i in range(1, len(str1) + 1):
        candidate = str1[0:i]
        if repeats(candidate, str1) and repeats(candidate, str2):
            biggestGCD = candidate
    return biggestGCD

#candidate = "ab"
#string = "abababab"
def repeats(candidate, string):
    # returns true if candidate is a repeat of string by some number of repeats
    idx = 0
    while idx < len(string):
        if idx + len(candidate) > len(string): # if the next candidate is too long, we overshot the end of the string
            return False
        if string[idx:idx+len(candidate)] != candidate: # if the next block doesn't match the candidate, we didn't find a repeat
            return False
        idx += len(candidate)
    return True