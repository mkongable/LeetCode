def groupThePeople(self, groupSizes):
    """
    :type groupSizes: List[int]
    :rtype: List[List[int]]
    """
    # make a dictionary linking people to their group size
    # loop through the dictionary breaking up the groups into lists of the group size
    # add lists to the total list
    # return the total list
    groupsizing = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] in groupsizing:
            groupsizing[groupSizes[i]].append(i)
        else:
            groupsizing[groupSizes[i]] = [i]
    total = []
    for key in groupsizing:
        for i in range(0, len(groupsizing[key]), key):
            total.append(groupsizing[key][i:i+key])
    return total