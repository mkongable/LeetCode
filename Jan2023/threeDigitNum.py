def largestGoodInteger(self, num):
    """
    :type num: str
    :rtype: str
    """
    # break string into chunks of 3
    # check if the integer is evenly divisible by 111
    # if it is, 
        # if int is greater than the current largest good integer, set the current largest good integer to int
    # return the current largest good integer
    max = ""
    for i in range(0, len(num) - 2):
        if int(num[i:i+3]) % 111 == 0:
            if max == "" or int(num[i:i+3]) > int(max):
                max = num[i:i+3]
    return max

num = "6777133339"
print(largestGoodInteger(any, num))
