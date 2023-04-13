def separateDigits(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # loop thru the list
    # if the element is greater than 10,
        # mod the element by 10 and add it as the next element in the list
        # divide the element by 10
        # add the quotient to the list
        # repeat until the element is less than 10
    # return the list
    idx = 0
    length = len(nums)
    while idx < length:
        while nums[idx] > 10:
            nums.insert(idx+1, nums[idx] % 10)
            nums[idx] = nums[idx] // 10
            length+=1
        idx+=1
    return nums

nums = [123, 456, 789]
print(separateDigits(nums))
