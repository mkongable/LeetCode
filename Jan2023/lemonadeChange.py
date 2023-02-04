def lemonadeChange(self, bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    # keep track of the number of 5's, 10's, and 20's
    # iterate through the bills
    # if the bill is a 5, increment the number of 5's
    # if the bill is a 10, increment the number of 10's and decrement the number of 5's by 1
    # if the bill is a 20, increment the number of 20's and decrement the number of 10's and 5's by 1
    # if no 10's are available, decrement the number of 5's by 3
    # if the number of 5's is 0, return false
    # return true

    # keep track of the number of 5's, 10's, and 20's
    fives = 0
    tens = 0
    twenties = 0
    # iterate through the bills
    for bill in bills:
        # if the bill is a 5, increment the number of 5's
        if bill == 5:
            fives += 1
        # if the bill is a 10, increment the number of 10's and decrement the number of 5's by 1
        elif bill == 10:
            tens += 1
            fives -= 1
        # if the bill is a 20, increment the number of 20's and decrement the number of 10's and 5's by 1
        elif bill == 20:
            twenties += 1
            if tens > 0:
                tens -= 1
                fives -= 1
            # if no 10's are available, decrement the number of 5's by 3
            else:
                fives -= 3
        # if the number of 5's is 0, return false
        if fives < 0:
            return False
    # return true
    return True