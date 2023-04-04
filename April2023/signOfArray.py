class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # loop thru keeping track of how many negative numbers there are
        # if there are an even number of negative numbers, return 1
        # if there are an odd number of negative numbers, return -1
        
        negatives = 0
        
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                negatives += 1
        if negatives % 2 == 0:
            return 1
        else:
            return -1