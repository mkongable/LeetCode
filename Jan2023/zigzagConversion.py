def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # create an ordered dictionary of rows to characters
    # iterate through the string
    # add the characters to the dictionary
    # if reached the bottom row, go up
    # if reached the top row, go down
    # return the string of characters in the dictionary in order of row
    # if numRows is 1, return the string
    if numRows == 1:
        return s
    rowsTochars = collections.OrderedDict()
    for i in range(numRows):
        rowsTochars[i] = []
    row = 0
    goingDown = True
    for char in s:
        rowsTochars[row].append(char)
        if row == numRows - 1:
            goingDown = False
        if row == 0:
            goingDown = True
        if goingDown:
            row += 1
        else:
            row -= 1
    zigzag = ""
    for row in rowsTochars:
        zigzag += "".join(rowsTochars[row])
    return zigzag

