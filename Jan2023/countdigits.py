def countDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    # Break number into digits
    # Test the number of digits that evenly divide the number
    # Return the number of digits that evenly divide the number
    count = 0
    for digit in str(num):
        if int(digit) != 0 and num % int(digit) == 0:
            count += 1
    return count