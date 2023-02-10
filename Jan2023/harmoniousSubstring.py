def findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # create a sorted dictionary of the number of times each number appears
    # if the next number in the dictionary is 1 greater see if the sum of times is greater than the current max
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    count = sorted(count.items())
    max = 0
    for i in range(len(count) - 1):
        if count[i+1][0] - count[i][0] == 1:
            if count[i+1][1] + count[i][1] > max:
                max = count[i+1][1] + count[i][1]
    return max

nums = [1,3,2,2,5,2,3,7]
print(findLHS(any, nums))
    