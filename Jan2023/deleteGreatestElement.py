def deleteGreatestValue(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # sort each row in the grid in decreasing order
    # take the max of each column and add to the total
    # return the total
    # if the grid is empty, return 0

    # sort each row in the grid in decreasing order
    for row in grid:
        row.sort(reverse=True)
    # take the max of each column and add to the total
    total = 0
    for i in range(len(grid[0])):
        max = 0
        for j in range(len(grid)):
            if grid[j][i] > max:
                max = grid[j][i]
        total += max
    # return the total
    return total