# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum = 0
        self.helper(root, False)
        return self.sum
    
    def helper(self, root, side):
        if not root.left and not root.right and side == True:
            self.sum += root.val
            return
        if root.left:
            self.helper(root.left, True)
        if root.right:
            self.helper(root.right, False)
            
