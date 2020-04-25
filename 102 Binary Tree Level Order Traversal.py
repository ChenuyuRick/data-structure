# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        line = []
        next_level = []
        while q:
            head = q.pop(0)
            if head.left:
                next_level.append(head.left)
            if head.right:
                next_level.append(head.right)
            line.append(head.val)
            if not q:
                res.append(line)
                if next_level:
                    q = next_level
                    line = []
                    next_level = []
        return res
