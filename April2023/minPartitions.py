def partitionString(self, s):
    """
    :type s: str
    :rtype: int
    """
    # create a set 
    # run forward in the string, adding each character to the set
        # if the character is already in the set, then we have a partition
            # add 1 to the partition count
            # empty the set
            # add the current character to the set
    # return the partition count
    
    partitionCount = 0
    lettersInCurrentPartition = set()
    for i in s:
        if i in lettersInCurrentPartition:
            partitionCount += 1
            lettersInCurrentPartition = set()
            lettersInCurrentPartition.add(i)
        else:
            lettersInCurrentPartition.add(i)
    return partitionCount + 1