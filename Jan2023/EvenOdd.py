def sortArrayByParity(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # create 2 lists, one for even, one for odd
    # loop thru nums to determine if even or odd
    # add to lists
    # return even + odd
    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd
        