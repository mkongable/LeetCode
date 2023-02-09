def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # if we are at the last index, we need 0 jumps to get to the finish
    # let OPT(i) be the minimum number of jumps to get to the end from index i
    # then, OPT(i) = the min OPT of everything that is currently in range of i