def findRestaurant(self, list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    # create a dictionary of list1 and list2
    # key: restaurant name, value: list of indices
    # if the restaurant name is in both lists, add the indices together
    # find the minimum sum of indices
    # add the names of the restaurants with the minimum sum of indices to a list
    # return the list
    restaurantToIndex = {}
    for(i, restaurant) in enumerate(list1):
        restaurantToIndex[restaurant] = [i]
    for(i, restaurant) in enumerate(list2):
        if(restaurant in restaurantToIndex):
            restaurantToIndex[restaurant].append(i)
    minSum = float('inf')
    result = []
    for restaurant in restaurantToIndex:
        if(len(restaurantToIndex[restaurant]) == 2):
            if sum(restaurantToIndex[restaurant]) < minSum:
                result = [restaurant]
                minSum = sum(restaurantToIndex[restaurant])
            elif sum(restaurantToIndex[restaurant]) == minSum:
                result = result + [restaurant]
    return result
            
    
    