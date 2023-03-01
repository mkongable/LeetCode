def sortArray(self, nums: List[int]) -> List[int]:
    heapq.heapify(nums) # Build a min-heap

    sorted_arr = []
    while nums:
        sorted_arr.append(heapq.heappop(nums)) # Extract the minimum element

    return sorted_arr