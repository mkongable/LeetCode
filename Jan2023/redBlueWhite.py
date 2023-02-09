def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # if the number is 0, move it to the front of the list
    # if the number is 2, move it to the end of the list
    # if the number is 1, leave it where it is
    idx = 0
    twoCount = 0
    while idx < len(nums):
        if nums[idx] == 0:
            nums.insert(0, nums.pop(idx))
            idx += 1
        elif nums[idx] == 2:
            nums.append(nums.pop(idx))
            twoCount += 1
            if idx >= len(nums) - twoCount:
                break
        else:
            idx += 1
    return nums
            
nums = [2,0,2,1,1,0]
print(sortColors(any, nums))
    