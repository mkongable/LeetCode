def shuffle(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    # create a new list
    # loop through nums with one pointer starting at 0 and one starting at n
    # add the value at the first pointer to the new list
    # add the value at the second pointer to the new list
    # return the new list
    l = []
    for i in range(n):
        l.append(nums[i])
        l.append(nums[i+n])
    return l