from typing import List

def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            # too high go down
            high = mid - 1
        elif nums[mid] < target:
            # too low go higher
            low = mid + 1
        else:
            # nums[mid] == target
            return mid
    return -1