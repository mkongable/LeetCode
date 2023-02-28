def getCommon(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    # loop thru both arrays
    # if nums1[i] == nums2[j], return nums1[i]
    # else, increment i or j based on which is smaller
    # if i or j is out of range, return -1
    pointer1 = 0
    pointer2 = 0
    while pointer1 < len(nums1) and pointer2 < len(nums2):
        if nums1[pointer1] == nums2[pointer2]:
            return nums1[pointer1]
        elif nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1
        else:
            pointer2 += 1
    return -1