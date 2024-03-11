from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            next_node = prev.next
            prev.next = current.next
            current.next = current.next.next
            prev.next.next = next_node

        return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    left = 2
    right = 4
    print(Solution().reverseBetween(head, left, right))

    head = ListNode(5)
    left = 1
    right = 1
    print(Solution().reverseBetween(head, left, right))

    head = ListNode(3, ListNode(5))
    left = 1
    right = 2
    print(Solution().reverseBetween(head, left, right))
