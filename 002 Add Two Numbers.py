# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        fake_head = ListNode(None)
        curr_node = fake_head
        carry = 0
        while head1 and head2:
            temp_sum = head1.val + head2.val + carry
            carry = temp_sum // 10
            curr_node.next = ListNode(temp_sum % 10)
            curr_node = curr_node.next
            head1 = head1.next
            head2 = head2.next
        while head1:
            temp_sum = head1.val + carry
            carry = temp_sum // 10
            curr_node.next = ListNode(temp_sum % 10)
            curr_node = curr_node.next
            head1 = head1.next
        while head2:
            temp_sum = head2.val + carry
            carry = temp_sum // 10
            curr_node.next = ListNode(temp_sum % 10)
            curr_node = curr_node.next
            head2 = head2.next
        if carry > 0:
            curr_node.next = ListNode(carry)
        return fake_head.next
    
    
    def reverse(self, node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
        
