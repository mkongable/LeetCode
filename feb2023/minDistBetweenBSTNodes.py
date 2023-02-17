def minDiffInBST(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # convert the BST to a sorted list
    # loop thru the list and find the min difference
    # return the min difference
    sorted_arr = inorder(root, [])
    min_diff = sorted_arr[1] - sorted_arr[0]
    for i in range(1, len(sorted_arr) - 1):
        diff = sorted_arr[i + 1] - sorted_arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff


def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)
    return arr