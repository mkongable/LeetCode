def alternateDigitSum(self, n):
    """
    :type n: int
    :rtype: int
    """
    # set the coefficient to -1 if the length of n is even, 1 if the length of n is odd
    # set the sum to 0
    # for each digit in n:
        # take the modulus of n by 10
        # multiply the modulus by the coefficient
        # add the result to the sum
        # divide n by 10
        # multiply the coefficient by -1
    # return the sum
    if len(str(n)) % 2 == 0:
        coefficient = -1
    else:
        coefficient = 1
    sum = 0
    while n > 0:
        sum += (n % 10) * coefficient
        n = n // 10
        coefficient *= -1
    return sum
    