def maximumCount(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # determine where the positive/negative boundary is
    # if the boundary is at the beginning or end of the list, return the length of the list
    # else, return max of the count of the positive numbers and the count of the negative numbers
    
    # if boundary is at the beginning or end of the list, return the length of the list
    if(nums[0] > 0 or nums[len(nums) - 1] < 0):
        return len(nums)
    # find the boundary in log(n) time
    # binary search to find the boundary
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    while(low < high):
        if nums[mid] < 0:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    
    
    