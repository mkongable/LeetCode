def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    for i in range(len(nums)):
        # check if i is the pivot by checking if the sum of the left side is equal to the sum of the right side
        if sum == sum(nums[i+1:]):
            return i
        else:
            sum += nums[i]
    return -1
    