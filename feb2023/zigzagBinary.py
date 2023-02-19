# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # need to populate a hashmap (dictionary) which maps the level to the list of nodes (left to right) at that level
        # then, iterate thru the hashmap and reverse the odd levels
        # then, return the values of the hashmap
        # assume dictionaries are ordered due to documentation
        
        if root is None:
            return []
        
        result_dict = self.populateHashmap(root, {}, 0)
        
        # reverse the odd levels
        TBR = [] # create list of lists where the list index is the level
        for key, value in result_dict.items():
            if key % 2 == 1:
                value.reverse()
            TBR.append(value)
        return TBR
        
        
        
    def populateHashmap(self, root, hashmap, level):
        # base case
        if root is None:
            return
        # recursive case
        # add the root to the hashmap
        # populate the left and right children
        # return the hashmap
        self.populateHashmap(root.left, hashmap, level + 1)
        
        # if hashmap level is empty, make it a new list containing the root.val
        if level not in hashmap:
            hashmap[level] = [root.val]
        else:
            hashmap[level].append(root.val)
            
        self.populateHashmap(root.right, hashmap, level + 1)
        return hashmap