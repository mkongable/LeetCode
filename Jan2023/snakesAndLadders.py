from typing import List

def getPosition(x, n):
    # n is the length of the board, x is the square number to get
    q, r = divmod(x - 1, n)
    return n - 1 - q, n - 1 - r if q % 2 else r

def snakesAndLadders(board: List[List[int]]) -> int:
    n = len(board)

    # convert the board to a 1D array
    oneD = [0] * (n * n)
    i = 0
    for x in range(1, n**2 + 1):
        row, col = getPosition(x, n)
        oneD[i] = board[row][col]
        i += 1

    # represent the board as a graph
    graph = {}
    for i in range(n * n):
        graph[i] = []
        for j in range(1, 7):
            if i + j < n * n:
                if oneD[i + j] == -1:
                    graph[i].append(i + j)
                else:
                    graph[i].append(oneD[i + j] - 1)

    # BFS
    queue = [(0, 0)]  # keep track of current node and the depth of that node
    visited = set()
    while queue:
        node, depth = queue.pop(0)
        if node == n * n - 1:
            return depth
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, depth + 1))

    return -1


board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]

print(snakesAndLadders(board))