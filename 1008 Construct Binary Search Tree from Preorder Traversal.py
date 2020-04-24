# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            Node = TreeNode(i)
            if Node.val < stack[-1].val:
                stack[-1].left = Node
                stack.append(Node)
            else:
                while stack and stack[-1].val < Node.val:
                    last = stack.pop()
                last.right = Node
                stack.append(Node)
        return root
