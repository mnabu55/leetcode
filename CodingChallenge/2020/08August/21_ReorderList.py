'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        node_list = []
        current = head
        while current is not None:
            node_list.append(current)
            current = current.next
        node_list_count = len(node_list)

        back_index = node_list_count - 1
        current = head
        for i in range(node_list_count // 2):
            next = current.next
            current.next = node_list.pop()
            current.next.next = next
            current  = current.next.next
        if current is not None:
            current.next = None

        current = head
        while current is not None:
            print('val: ', current.val)
            current = current.next


l5 = ListNode(5, None)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

solution = Solution()
solution.reorderList(l1)
