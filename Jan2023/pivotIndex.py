def pivotInteger(self, n):
    """
    :type n: int
    :rtype: int
    """
    # create a list of integers from 1 to n
    # using two pointers, start at the beginning and end of the list
    # while the pointers are not equal
        # if the sum at the beginning is less than the end, move the beginning pointer up
        # if the sum at the end is less than the beginning, move the end pointer down
    # if the pointers are equal, return the index if the sums are equal
    # else, return -1
    l = [i for i in range(1, n+1)]
    begin = 0
    end = len(l) - 1
    sumBegin = 0
    sumEnd = 0
    while begin != end:
        if sumBegin < sumEnd:
            sumBegin += l[begin]
            begin += 1
        else:
            sumEnd += l[end]
            end -= 1
    if sumBegin == sumEnd:
        return begin + 1 # +1 because the index is 0 based
    else:
        return -1