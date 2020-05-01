# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        res = []
        self.helper(root, 0, res)
        return sum in res
        
    def helper(self, root, sum_num, res):
        sum_num += root.val
        if root.left:
            self.helper(root.left, sum_num, res)
        if root.right:
            self.helper(root.right, sum_num, res)
        if not root.left and not root.right:
            res.append(sum_num)
