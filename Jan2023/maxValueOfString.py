def maximumValue(self, strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    # Loop through strings
    # If string contains only a-z or a-z and a number, compare length to max
    # If string is only numbers, convert to int and compare to max
    max = 0
    for string in strs:
        if string.isalpha():
            if len(string) > max:
                max = len(string)
        elif string.isdigit():
            if int(string) > max:
                max = int(string)
        elif string.isalnum():
            if len(string) > max:
                max = len(string)
    return max

strs = ["1","01","001","0001", "Alic3", "4RE"]
print(maximumValue(any, strs))