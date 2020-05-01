# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Wrapper:
    def __init__(self, isUniTree=None, count = 0):
        self.isUniTree = None
        self.count = 0
        
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = self.helper(root)
        return res.count
    
    
    def helper(self, root):
        res = Wrapper(None, 0)
        if root.left is None and root.right is None:
            res.isUniTree = True
        elif root.left is None: 
            res_right = self.helper(root.right)
            res.isUniTree = (root.val == root.right.val) and res_right.isUniTree
            res.count = res_right.count  
        elif root.right is None:
            res_left = self.helper(root.left)
            res.isUniTree = (root.val == root.left.val) and res_left.isUniTree
            res.count = res_left.count
        else:
            res_left = self.helper(root.left)
            res_right = self.helper(root.right)
            res.isUniTree = (root.left.val == root.right.val == root.val) and res_left.isUniTree and res_right.isUniTree
            res.count = res_left.count + res_right.count
        if res.isUniTree:
                res.count += 1   
        return res
