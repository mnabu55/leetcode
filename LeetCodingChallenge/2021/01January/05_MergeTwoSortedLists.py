'''

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 is [] or l1 is None) and (l2 is [] or l2 is None):
            return None
        elif l1 is [] or l1 is None:
            return l2
        elif l2 is [] or l2 is None:
            return l1
        head = current = None
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        current = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1 is None:
            current.next = l2
        else:
            current.next = l1
        return head

    def print_all(self, l1: ListNode):
        while l1 is not None:
            print("value: ", l1.val)
            l1 = l1.next


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

solution = Solution()
solution.mergeTwoLists(l1_1, l2_1)
