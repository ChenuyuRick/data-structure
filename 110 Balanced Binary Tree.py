# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.judge = True
        self.helper(root)
        return self.judge
    
   
    def helper(self, root):
        if not root:
            return 0
        left_height = self.helper(root.left)
        right_height = self.helper(root.right)
        if abs(left_height - right_height) > 1:
            self.judge = False
        return 1 + max(left_height, right_height)
