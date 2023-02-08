def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    # if the dividend is 0, return 0
    if dividend == 0:
        return 0
    # if the absolute value of the dividend is less than the absolute value of the divisor, return 0
    if abs(dividend) < abs(divisor):
        return 0
    counter = 0
    absdividend = abs(dividend)
    absdivisor = abs(divisor)
    # while the absolute value of the dividend is greater than or equal to the absolute value of the divisor
    while(absdividend >= absdivisor):
        if(absdivisor == 1):
            counter = absdividend
            break
        absdividend -= absdivisor
        counter += 1
    # if the dividend and divisor are the same sign, return the counter
    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        return counter
    else:
        return -counter
    
print(divide(any, -2147483648, -1))