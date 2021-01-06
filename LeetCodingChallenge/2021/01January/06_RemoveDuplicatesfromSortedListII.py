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

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-1)

        start = head
        dummy = dummy_head
        while head is not None:
            start = head
            count = 0
            while head is not None and head.val == start.val:
                head = head.next
                count += 1
            if count > 1:
                start = head
            else:
                dummy.next = start
                dummy = dummy.next
        dummy.next = None
        return dummy_head.next


solution = Solution()
l = solution.create_linkedList([1,2,3,3,4,4,5])
solution.print_all(l)

res = solution.deleteDuplicates2(l)
solution.print_all(res)


# n1 = ListNode(1)
# n2 = ListNode(1)
# n3 = ListNode(1)
# n4 = ListNode(2)
# n5 = ListNode(3)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
#
# res = solution.deleteDuplicates(n1)
# solution.print_all(res)
#
#
#
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(3)
# n5 = ListNode(4)
# n6 = ListNode(4)
# n7 = ListNode(5)
#
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# res = solution.deleteDuplicates(n1)
# solution.print_all(res)
