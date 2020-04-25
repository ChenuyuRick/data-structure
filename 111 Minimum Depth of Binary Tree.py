# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.minDepth(root.left) if root.left is not None else float('inf')
        right = self.minDepth(root.right) if root.right is not None else float('inf')
        return min(left, right) + 1
