# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.base_root = root
        self.cur_root = root
        self.stack = []
        self.has_next_node = self.base_root is not None
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack or self.cur_root:
            while self.cur_root:
                self.stack.append(self.cur_root)
                self.cur_root = self.cur_root.left
            self.cur_root = self.stack.pop()
            record = self.cur_root
            self.cur_root = self.cur_root.right
            break
        if len(self.stack) == 0 and record.right is None:
            self.has_next_node = False
        return record.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """ 
        return self.has_next_node
