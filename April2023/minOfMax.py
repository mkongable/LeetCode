class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set currentMin to the first element in the array
        # loop through the array
            # if average of nums[i] and nums[i+1] is greater than currentMin
                # set currentMin to the average of nums[i] and nums[i+1]
        # return currentMin
        currentMin = nums[0]
        for i in range(len(nums)-1):
            if (nums[i] + nums[i+1]) / 2 > currentMin:
                currentMin = (nums[i] + nums[i+1]) / 2
        return currentMin