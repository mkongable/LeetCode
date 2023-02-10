def minCostToMoveChips(self, position):
    """
    :type position: List[int]
    :rtype: int
    """
    # if the length of the list is 1, return 0
    # create a list of costs for each position
    # for each position
        # if the number is odd, add 1 to the cost of the even positions
        # if the number is even, add 1 to the cost of the odd positions
    # return the minimum cost
    if len(position) == 1:
        return 0
    cost = [0] * len(position)
    for i in range(len(position)):
        for j in range(len(position)):
            if position[i] % 2 == 0:
                if position[j] % 2 == 1:
                    cost[i] += 1
            else:
                if position[j] % 2 == 0:
                    cost[i] += 1
    return min(cost)

position = [1,2,3,5]
print(minCostToMoveChips(any, position))