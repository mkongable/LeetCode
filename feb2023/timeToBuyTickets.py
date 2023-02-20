def timeRequiredToBuy(self, tickets, k):
    """
    :type tickets: List[int]
    :type k: int
    :rtype: int
    """
    time = 0
    # everyone ahead of the index can buy at most tickets[index] tickets
    # everyone behind the index can buy at most tickets[index] - 1 tickets
    desiredtickets = tickets[k]
    for i in range(k + 1):
        time += min(desiredtickets, tickets[i])
    for i in range(k + 1, len(tickets)):
        time += min(desiredtickets - 1, tickets[i])
    return time