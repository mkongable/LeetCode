def maximumTime(self, time):
    """
    :type time: str
    :rtype: str
    """
    #first digit
        # if the first digit is a ?, check the second digit
            # if the second digit is a ?, set the first digit to 2
            # if the second digit is a 0, 1, 2, 3, set the first digit to 2
            # if the second digit is a 4, 5, 6, 7, 8, 9, set the first digit to 1
        # if the first digit is a 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, do nothing
    #second digit
        # if the first digit is a 2, check the second digit
            # if the second digit is a ?, set the second digit to 3
        # if the first digit is a 0, 1 set the second digit to 9
    # third digit
        # if the third digit is a ?, set the third digit to 5
    # fourth digit
        # if the fourth digit is a ?, set the fourth digit to 9
    # return the time
    if time[0] == '?':
        if time[1] == '?':
            time = '2' + time[1:]
        elif int(time[1]) < 4:
            time = '2' + time[1:]
        else:
            time = '1' + time[1:]
    if time[1] == '?':
        if time[0] == '2':
            time = time[0] + '3' + time[2:]
        else:
            time = time[0] + '9' + time[2:]
    if time[3] == '?':
        time = time[:3] + '5' + time[4:]
    if time[4] == '?':
        time = time[:4] + '9'
    return time
            