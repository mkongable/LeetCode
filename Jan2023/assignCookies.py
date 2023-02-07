def findContentChildren(self, g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    # sort the lists
    # create a counter
    # working from the back
        # if the last cookie is greater than or equal to the last child
            # increment the counter
            # remove the last cookie and child
        # else
            # remove the last child
    # return the counter
    g.sort()
    s.sort()
    counter = 0
    for i in range(len(g)):
        # check if cookies or kids are empty
        if len(s) == 0 or len(g) == 0:
            return counter
        if s[-1] >= g[-1]:
            counter += 1
            s.pop()
            g.pop()
        else:
            g.pop()
    return counter