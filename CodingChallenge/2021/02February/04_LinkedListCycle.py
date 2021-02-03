'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
'''
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def makeList(self, l1: List) -> ListNode:
        dummy_head = ListNode(-1)
        current = dummy_head
        for val in l1:
            current.next = ListNode(val)
            current = current.next
        return dummy_head.next

    def print(self, l: ListNode) -> None:
        while l:
            print("val: ", l.val)
            l = l.next


solution = Solution()
l3 = ListNode(3)
l2 = ListNode(2)
l0 = ListNode(0)
lm4 = ListNode(-4)
l3.next = l2
l2.next = l0
l0.next = lm4
lm4.next = l2

l1 = ListNode(1)
l1.next = l2
l2.next = None

print(solution.hasCycle(l1))
