def maxDistance(self, colors):
    """
    :type colors: List[int]
    :rtype: int
    """
    # create two pointers, one at the beginning and one at the end
    # while the pointers are not at the same index
        # if the colors at the pointers are the same
            # move back pointer to the next index
        # else
            # return distance between the pointers
    # return 0
    endPT = len(colors) - 1
    endMax = 0
    # start from the beginning and compare to end distance
    for i in range(len(colors)):
        # if colors are different
        if colors[endPT] != colors[i]:
            # return distance between the pointers
            endMax = endPT - i
            break
    beginPT = 0
    beginMax = 0
    for i in range(len(colors) - 1, -1, -1):
        if colors[beginPT] != colors[i]:
            beginMax = i - beginPT
            break
    return max(beginMax, endMax)
    
colors = [4,4,4,11,4,4,11,4,4,4,4,4]
print(maxDistance(any, colors))