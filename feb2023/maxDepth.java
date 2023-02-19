public int maxDepth(TreeNode root) {
    //want to get the max depths going down the left and the right children
    //compare them and return the higher of the two
    int leftDepth = 0;
    int rightDepth = 0;
    if (root == null) {
        return 0;
    }
    if (root.left != null) {
        leftDepth = maxDepth(root.left);
    }
    if (root.right != null) {
        rightDepth = maxDepth(root.right);
    }
    return Math.max(leftDepth, rightDepth) + 1;
}