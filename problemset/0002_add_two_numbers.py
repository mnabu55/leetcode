# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        l = dummy_head
        carry = 0

        while l1 is not None or l2 is not None:
            sum_value = carry
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next

            l.next = ListNode(sum_value % 10)
            l = l.next
            carry = sum_value // 10

        if carry != 0:
            l.next = ListNode(carry)

        return dummy_head.next
