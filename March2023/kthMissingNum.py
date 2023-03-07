def findKthPositive(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    # loop thru the array
    # keep count of missing numbers
    # if missing >= k:
        # return k
    # if arr[0] != 1:
        # missing = arr[0] - 1
    # else:
        # missing = 0
    missing = 0
    if arr[0] != 1:
        missing = arr[0] - 1
        if missing >= k:
            return k
    for i in range(len(arr) - 1): 
        if arr[i + 1] - arr[i] > 1:
            missing += arr[i + 1] - arr[i] - 1
            if missing >= k:
                return arr[i] + (k - (missing - (arr[i + 1] - arr[i] - 1)))
    if missing < k:
        return arr[-1] + k - missing
    

arr = [2,3,4,7,11]
print(findKthPositive(any, arr, 5))