def isMonotonic(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # loop thru the array
    # if it is increasing
        # set increasing to true
    # if it is decreasing
        # set decreasing to true
    # if increasing and decreasing are true
        # return false
    # if increasing or decreasing are true
        # return true
    increasing = False
    decreasing = False
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            increasing = True
        if nums[i] > nums[i + 1]:
            decreasing = True
        if increasing and decreasing:
            return False
    return True
    
    