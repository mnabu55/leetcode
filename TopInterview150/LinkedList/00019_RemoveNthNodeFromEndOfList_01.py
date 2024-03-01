from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head


def makeList(nums: List) -> ListNode:
    dummy_head = ListNode(-1)
    current = dummy_head
    for val in nums:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def printLinkedList(node: ListNode) -> None:
    print('---------------------------------')
    
    while node:
        print(f'[{node.val}]', end=' -> ')
        node = node.next
    
    print('', end='\n')


solution = Solution()

nums = [x for x in range(1, 6)]
head = makeList(nums)
printLinkedList(head)
head = solution.removeNthFromEnd(head, 2)
printLinkedList(head)

nums = [x for x in range(1, 2)]
head = makeList(nums)
printLinkedList(head)
head = solution.removeNthFromEnd(head, 1)
printLinkedList(head)

nums = [x for x in range(1, 3)]
head = makeList(nums)
printLinkedList(head)
head = solution.removeNthFromEnd(head, 1)
printLinkedList(head)
