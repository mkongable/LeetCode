def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # initialize the perimeter
    # iterate through the grid
        # if the current node is land
            # check surrounding nodes for land
            # add the number of 0's around the 1's to the perimeter
    # return the perimeter
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if i < len(grid)-1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j < len(grid[0])-1 and grid[i][j+1] == 1:
                    perimeter -= 1
    return perimeter

grid = [[1,0,1], [1,1,1]]
print(islandPerimeter(any, grid))
    