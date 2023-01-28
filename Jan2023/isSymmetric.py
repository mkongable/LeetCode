from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        if root.left and root.right:
            return self.isMirror(root.left, root.right)
        else:
            return False
    
    def isMirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return self.isMirror(root1.right, root2.left) and self.isMirror(root1.left and root2.right)
            else:
                return False
        else:
            return False