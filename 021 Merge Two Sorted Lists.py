# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        fake_head = ListNode(None)
        Node = fake_head
        while l1 and l2:
            if l1.val < l2.val:
                Node.next = l1
                l1 = l1.next
            else:
                Node.next = l2
                l2 = l2.next
            Node = Node.next
        if l1:
            Node.next = l1
        if l2:
            Node.next = l2
        return fake_head.next
