def maxSubsequence(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # take a chunk of k elements from nums
    # if nums[i] > min(chunk), replace min(chunk) with nums[i]
    largest = [x for x in nums[:k]]
    for i in range(k, len(nums)):
        if nums[i] > min(largest):
            #remove min(largest) from largest
            largest.remove(min(largest))
            # add nums[i] to largest
            largest.append(nums[i])
    return largest

nums = [9, 5, 3, 6, 7, 8]
print(maxSubsequence(any, nums, 3))
    