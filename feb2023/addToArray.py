def addToArrayForm(self, num, k):
    """
    :type num: List[int]
    :type k: int
    :rtype: List[int]
    """
    # add k to the num[-1]
    # take the modulus and place it in the num[-1]
    # divide k by 10
    # loop thru until k is 0
    counter = len(num) - 1
    while k > 0:
        if counter < 0:
            k_list = [int(i) for i in str(k)]
            num = k_list + num
            break
        else:
            num[counter] += k
            k = num[counter] // 10
            num[counter] %= 10
            counter-= 1
    return num

num = [0]
print(addToArrayForm(any, num, 10000))