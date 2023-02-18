def findPoisonedDuration(self, timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    # loop thru timeSeries
        # if timeSeries[i] + duration > timeSeries[i+1]
            # add timeSeries[i+1] - timeSeries[i]
        # else
            # add duration
    if len(timeSeries) == 0:
        return 0
    posionTime = 0
    for i in range(len(timeSeries)-1):
        if timeSeries[i] + duration > timeSeries[i+1]:
            posionTime += timeSeries[i+1] - timeSeries[i]
        else:
            posionTime += duration
    return posionTime + duration # add the last duration