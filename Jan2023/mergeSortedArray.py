def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # loop thru both lists
    # if the first list is empty, add the rest of the second list
    # if the second list is empty, return the first list
    # else
        # if the first element of the first list is less than the first element of the second list
            # move pointer to next element in first list
        # else
            # insert the current element of the second list into the first list
            # shift the remaining first list elements to the right
            # move pointer to next element in second list
    # return the first list
    L1pointer = 0
    L2pointer = 0
    while L1pointer < m and L2pointer < n:
        if nums1[L1pointer] < nums2[L2pointer]:
            L1pointer += 1
        else:
            nums1.insert(L1pointer, nums2[L2pointer]) 
            L2pointer += 1
            L1pointer += 1
            m += 1
            nums1.pop()
    if L2pointer < n:
        # remove the 0s from the end of the list
        for i in range(n - L2pointer):
            nums1.pop()
        # add the rest of the second list
        nums1.extend(nums2[L2pointer:])
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(any, nums1, 3, nums2, 3))