# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        subset = []
        self.helper(root, subset, 0, sum)
        return self.result
        
    def helper(self, root, subset, sum_num, sum): 
        subset.append(root.val)
        sum_num += root.val
        if root.left is None and root.right is None:
            if sum_num == sum:
                self.result.append(subset[:])
        if root.left:
            self.helper(root.left, subset, sum_num, sum)
        if root.right:
            self.helper(root.right, subset, sum_num, sum)
        subset.pop()
