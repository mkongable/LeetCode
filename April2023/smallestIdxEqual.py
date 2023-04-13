class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # loop through the list
        # for each element, check if the modulus of the element is equal to the index
        # if it is, return the element
        # if we get to the end of the list, return -1
        for i in range(len(nums)):
            if nums[i] % 10 == i:
                return nums[i]
        return -1