def findMaximizedCapital(self, k, w, profits, capital):
    """
    :type k: int
    :type w: int
    :type profits: List[int]
    :type capital: List[int]
    :rtype: int
    """
    # use two priority queues
    # when a project is done, new possibilities for projects are opened
    # let projects be a priority queue that initially holds all the projects as tuples (capital, profit)
    # let available be a priority queue that initially holds no projects
    # pop all the projects from projects that have capital less than or equal to w and store them in available as tuples (-profit, capital)
    # do k times:
    #   do the project with the highest profit in available. Use the accumulated capital to update w and open up new projects from projects
    # return the accumulated capital
    import heapq

    projects = [(c, -p) for c, p in zip(capital, profits)]
    available = []
    heapq.heapify(projects)
    for _ in range(k):
        while projects and projects[0][0] <= w:
            heapq.heappush(available, heapq.heappop(projects)[1])
        w += -heapq.heappop(available) if available else 0
    return w
    