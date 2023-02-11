def findMaxAverage(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    # initialize the max average
    # initialize the current sum
    # iterate through the nums
        # add the current num to the current sum, removing the first num if the window is full
        # if the current sum/k is greater than the max average
            # set the max average to the current sum/k
    # return the max average
    # if k is equal to the length of nums, return the average of nums
    if k == len(nums):
        return sum(nums)/k
    maxAvg = -float('inf')
    currSum = 0
    for i in range(len(nums)):
        currSum += nums[i]
        if i >= k:
            currSum -= nums[i-k]
        if currSum/k > maxAvg and i >= k-1:
            maxAvg = currSum/k
    return maxAvg

nums = [9,7,3,5,6,2,0,8,1,9]
print(findMaxAverage(any, nums, 6))