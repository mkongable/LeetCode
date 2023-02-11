def largestOddNumber(self, num):
    """
    :type num: str
    :rtype: str
    """
    # while the last digit is even
        # remove the last digit
    # return num
    while len(num) > 0 and int(num[-1]) % 2 == 0:
        num = num[:-1]
    return num