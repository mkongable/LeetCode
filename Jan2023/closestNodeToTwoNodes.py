from typing import List

def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    # create a graph
    # run BFS from the node1 and save the distance from node 1 to all other nodes, distance is -1 by default until hit by BFS
    # run BFS from the node2 and save the distance from node 2 to all other nodes, distance is -1 by default until hit by BFS
    # run through the distances of each node from node 1 and node 2 and min the maxes with an O(n) loop
    # return the min of the maxes

    # create a graph
    # edges is already a graph

    distancesFromNode1 = [-1] * len(edges)
    distancesFromNode2 = [-1] * len(edges)
    visited = set()

    # run BFS from the node1 and save the distance from node 1 to all other nodes, distance is -1 by default until hit by BFS
    queue = [(node1, 0)]
    while queue:
        node, distance = queue.pop(0)  # get the next node from queue
        visited.add(node)  # mark the node as visited
        distancesFromNode1[node] = distance  # save the distance from node1 to this node
        for neighbor in [edges[node]]:  # add all the neighbors of this node to the queue
            if neighbor is not -1 and neighbor not in visited:
                queue.append((neighbor, distance + 1))

    visited = set()

    # run BFS from the node2 and save the distance from node 2 to all other nodes, distance is -1 by default until hit by BFS
    queue = [(node2, 0)]
    while queue:
        node, distance = queue.pop(0)
        visited.add(node)
        distancesFromNode2[node] = distance
        for neighbor in [edges[node]]:
            if neighbor is not -1 and neighbor not in visited:
                queue.append((neighbor, distance + 1))

    # run through the distances of each node from node 1 and node 2 and min the maxes with an O(n) loop
    minMax = float('inf')
    closest_node = -1
    for i in range(len(distancesFromNode1)):
        if distancesFromNode1[i] is not -1 and distancesFromNode2[i] is not -1:
            max_distance = max(distancesFromNode1[i], distancesFromNode2[i])
            if max_distance < minMax:
                minMax = max_distance
                closest_node = i
    
    return closest_node


print(closestMeetingNode([2,2,3,-1], 0, 1))