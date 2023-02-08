def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # make an OPT table
    # OPT[i] = the minimum number of jumps to get from the beginning to index i
    # OPT[0] = 0
    # Have nums[i] scan forward and update unfilled entries in range
    # return OPT[-1]
    OPT = [0] * len(nums)
    for i in range(len(nums)): # i is the index
        for j in range(i+1, i+nums[i]+1): # j is the index to jump to
            if j < len(nums): # if j is in range
                if OPT[j] == 0: # if j has not been filled
                    OPT[j] = OPT[i] + 1 # fill j with the minimum number of jumps to get to i + 1
        if OPT[-1] != 0:
            break
    return OPT[-1]

nums = [2,3,1,1,4]
print(jump(any, nums))