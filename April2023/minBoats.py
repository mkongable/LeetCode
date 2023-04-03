def numRescueBoats(self, people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    # sort the people
    # if people[0] + people[-1] > limit, then the last person has to be in a boat by himself
        # add 1 to boat, and remove the last person from the list
    # if people[0] + people[-1] <= limit, then the first and last person can be in the same boat
        # add 1 to boat, and remove the first and last person from the list
    # return boat
    
    # sort the people
    people.sort()
    boat = 0
    
    while people:
        if people[0] + people[-1] > limit:
            people.pop()
            boat += 1
        elif len(people) == 1:
            people.pop()
            boat += 1
        else:
            people.pop(0)
            people.pop()
            boat += 1
    return boat

print(numRescueBoats(any, [2,4], 5))
