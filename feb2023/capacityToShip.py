def shipWithinDays(self, weights, days):
    """
    :type weights: List[int]
    :type days: int
    :rtype: int
    """
    # given an input capacity, determine if it is possible to ship all items in the given number of days
    def possible(capacity):
        ships = 0
        ship_weight = 0
        for weight in weights:
            if ship_weight + weight > capacity:
                if weight > capacity: # the weight of the next item is greater than ship capacity
                    return False
                ships += 1
                ship_weight = 0
            ship_weight += weight
        if ship_weight > 0:
            ships += 1
        return ships <= days

    # binary search for the minimum capacity
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        if possible(mid):
            right = mid
        else:
            left = mid + 1
    
    return left