# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        return max(left + right, ldiameter, rdiameter)
        
    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1
