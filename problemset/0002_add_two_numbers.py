'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        sum_value = cur1.val + cur2.val
        top = current = ListNode(sum_value % 10)
        carry_up = sum_value // 10

        while True:
            sum_value = carry_up
            if cur1.next is None and cur2.next is None and carry_up == 0:
                break
            if cur1.next is not None:
                cur1 = cur1.next
                sum_value += cur1.val
            if cur2.next is not None:
                cur2 = cur2.next
                sum_value += cur2.val
            carry_up = sum_value // 10

            next = ListNode(sum_value % 10)
            current.next = next
            current = current.next

        return top
