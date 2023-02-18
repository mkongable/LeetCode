def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    # do all the swapping on the left child's children
    # do all the swapping on the right child's children
    # swap the left and the right child
    if root is None:
        return
    swapped_left = self.invertTree(root.left)
    swapped_right = self.invertTree(root.right)
    root.left = swapped_right
    root.right = swapped_left
    return root