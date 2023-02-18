def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # convert the strings to arrays
    # loop thru the arrays backwards
        # add the values of the arrays
        # if the sum is greater than 9
            # add 1 to the next value
            # subtract 10 from the sum
        # add the sum to the result
    # return the result
    nums1 = [int(i) for i in num1]
    nums2 = [int(i) for i in num2]
    result = ""
    # append 0s to the front of the shorter array
    if len(nums1) > len(nums2):
        for i in range(len(nums1) - len(nums2)):
            nums2.insert(0, 0)
    elif len(nums2) > len(nums1):
        for i in range(len(nums2) - len(nums1)):
            nums1.insert(0, 0)
    for i in range(len(nums1) - 1, -1, -1):
        sum = nums1[i] + nums2[i]
        if sum > 9 and i > 0:
            nums1[i - 1] += 1
            sum -= 10
        result = str(sum) + result
    return result
    
num1 = "1"
num2 = "9"
print(addStrings(any, num1, num2))