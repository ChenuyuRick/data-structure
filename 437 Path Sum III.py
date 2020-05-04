# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.result = 0
        freq = collections.defaultdict(int)
        freq[0] = 1
        self.dfs(root, 0, freq, sum)
        return self.result
    
    def dfs(self, root, Pathsum, freq, sum):
        if root:
            Pathsum += root.val
            self.result += freq[Pathsum - sum]
            freq[Pathsum] += 1
            
            self.dfs(root.left, Pathsum, freq, sum)
            self.dfs(root.right, Pathsum, freq, sum)
            
            freq[Pathsum] -= 1
