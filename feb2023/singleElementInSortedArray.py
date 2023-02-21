def singleNonDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # mimic binary search
    # if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1], then mid is the single element
    # elif nums[mid] == nums[mid-1] and mid is even, then the single element is on the left
    # else if nums[mid] == nums[mid+1] and mid is odd, then the single element is on the left
    # else, element is on the right
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while left < right:
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        elif nums[mid] == nums[mid-1] and mid % 2 == 0:
            right = mid - 1
        elif nums[mid] == nums[mid+1] and mid % 2 == 1:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return nums[mid]


nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(any, nums))