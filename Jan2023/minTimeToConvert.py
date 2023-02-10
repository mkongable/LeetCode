def convertTime(self, current, correct):
    """
    :type current: str
    :type correct: str
    :rtype: int
    """
    # check how many minutes are in the current time and how many minutes are in the correct time
    # if current[minutes] > correct[minutes],
        # add 1 to the hour
        # find how many times 15 minutes can be subtracted from the difference between the minutes
        # add the number of times 15 minutes can be subtracted from the difference between the minutes to the total
        # repeat with 5 and 1 minute(s)
    # if current[minutes] < correct[minutes],
        # find how many times 15 minutes can be subtracted from the difference between the minutes
        # add the number of times 15 minutes can be subtracted from the difference between the minutes to the total
        # repeat with 5 and 1 minute(s)
    # add the difference between the hours to the total
    total = 0
    # if current[minutes] > correct[minutes],
    if current[3:] > correct[3:]:
        minutediff = int(correct[3:]) + 60 - int(current[3:])
        hours = int(current[:2]) + 1
        if hours > 9:
            current = str(hours) + current[2:]
        else:
            current = '0' + str(hours) + current[2:]
        total = total + minutediff // 15
        minutediff = minutediff % 15
        total = total + minutediff // 5
        minutediff = minutediff % 5
        total = total + minutediff % 5
    # if current[minutes] < correct[minutes],
    elif current[3:] < correct[3:]:
        minutediff = abs(int(correct[3:]) - int(current[3:]))
        total = total + minutediff // 15
        minutediff = minutediff % 15
        total = total + minutediff // 5
        minutediff = minutediff % 5
        total = total + minutediff % 5
    total = total + abs(int(current[:2]) - int(correct[:2]))
    return total

current = "04:00"
correct = "06:05"
print(convertTime(any, current, correct))
