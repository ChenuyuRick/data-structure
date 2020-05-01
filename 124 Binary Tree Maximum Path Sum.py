# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_sum = float('-inf')
        self.helper(root)
        return self.max_sum
    
    def helper(self, root):
        if not root:
            return 0
        value = root.val
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.max_sum = max(self.max_sum, value + left, value + right, value + left + right, value)
        return max(value + left, value + right, value)
