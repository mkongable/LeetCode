def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # Loop through t
        # If the character at t[i] is the same as the character at s[0], pop s[0]
    # if s is empty, return True
    for i in range(len(t)):
        if t[i] == s[0]:
            s = s[1:]
        if len(s) == 0:
            return True
    return False
        