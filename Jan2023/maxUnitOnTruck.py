def maximumUnits(self, boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    # sort the boxTypes by the number of units in each box in decreasing order
    # keep track of the number of boxes in the truck
    # keep track of the total number of units in the truck
    # iterate through the boxTypes

    # sort in decreasing order
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    # keep track of the number of boxes in the truck
    boxesInTruck = 0
    # keep track of the total number of units in the truck
    totalUnits = 0
    # iterate through the boxTypes
    for box in boxTypes:
        # can take the whole stack of boxes
        if boxesInTruck + box[0] <= truckSize: 
            boxesInTruck += box[0]
            totalUnits += box[0] * box[1]
        # can only take a part of the stack of boxes
        else:
            totalUnits += (truckSize - boxesInTruck) * box[1]
            break
    return totalUnits
