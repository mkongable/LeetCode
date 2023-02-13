def licenseKeyFormatting(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # loop thru the string
        # remove the dashes
    # check if the length of the string is evenly divisible by k
    # if not, break the front off in the remainder
    # loop thru the string
        # seperate the string into groups of k with dashes
    # return the string
    s = s.replace("-", "")
    # work the way forward from the back, placing dashes every k characters
    for i in range(len(s) - k, 0, -k):
        s = s[:i] + "-" + s[i:]
    return s.upper()

s = "5F3Z-2e-9-w-23r33"
print(licenseKeyFormatting(any, s, 4))