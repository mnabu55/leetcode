'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        dummy = dummy_head
        while head is not None:
            start_element = head
            count = 0
            while head is not None and head.val == start_element.val:
                head = head.next
                count += 1

            if count > 1:               # if duplicate, skip this element
                start_element = head
            else:
                dummy.next = start_element
                dummy = dummy.next
        dummy.next = None
        return dummy_head.next

    def create_linkedList(self, array) -> ListNode:
        head = ListNode(array[0])
        current = head
        for v in array[1:]:
            current.next = ListNode(v)
            current = current.next
        return head

    def print_all(self, head: ListNode) -> None:
        print("---print_all---")
        current = head
        while current is not None:
            print("val: ", current.val)
            current = current.next


solution = Solution()
l = solution.create_linkedList([1,2,3,3,4,4,5])
solution.print_all(l)
