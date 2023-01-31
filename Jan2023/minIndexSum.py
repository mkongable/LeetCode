def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    # create inverse hashmap for list1, mapping element to index
    string2idx = {list1[i] : i for i in range(len(list1))}

    # traverse list2, to find the minimum index sum
    minSum = len(list1) + len(list2)
    for i in range(len(list2)):
        if list2[i] in string2idx:
            minSum = min(minSum, i + string2idx[list2[i]])

    # traverse list2 again, to find the elements with the minimum index sum
    res = []
    for i in range(len(list2)):
        if list2[i] in string2idx and i + string2idx[list2[i]] == minSum:
            res.append(list2[i])

    return res


# test the function
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1, list2))
