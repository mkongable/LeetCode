def maxDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # the source nodes are land nodes
    # we run BFS, for every iteration of BFS, we add all unexplored adjacent nodes to the growing mass of explored nodes and increment the distance searched by 1
    # as soon as the queue is empty, so return the distance searched
    
    # first check if there are no land nodes or no water nodes
    if not any(1 in row for row in grid) or not any(0 in row for row in grid):
        return -1

    # initialize the queue with all the land nodes
    queue = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                queue.append((i,j))

    # initialize the level
    level = 0
    while queue:
        # increment the level
        level += 1
        # get the size of the queue
        size = len(queue)
        # iterate through the queue
        for _ in range(size):
            # pop the first node
            node = queue.pop(0)
            # get the neighbors of the node
            neighbors = [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]
            # iterate through the neighbors
            for neighbor in neighbors:
                # check if the neighbor is in bounds
                if neighbor[0] < 0 or neighbor[0] >= len(grid) or neighbor[1] < 0 or neighbor[1] >= len(grid[0]):
                    continue
                # check if the neighbor is water
                if grid[neighbor[0]][neighbor[1]] == 0:
                    # set the neighbor to land
                    grid[neighbor[0]][neighbor[1]] = 1
                    # add the neighbor to the queue
                    queue.append(neighbor)

    # return the level
    return level - 1

grid = [[1,0,1],[0,0,0],[0,0,1]]
print(maxDistance(any, grid))