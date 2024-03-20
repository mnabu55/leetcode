from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight_wa(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        不正解： k がリストの数より大きいとうまく動かない
        """
        if k <= 0:
            return head

        slow = fast = head
        for _ in range(k):
            if fast:
                fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head
        head = slow.next
        slow.next = None

        return head

    def rotateRight_tle(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        １個ずつずらす作業を繰り返す
        tle
        """
        if not head or not head.next or k <= 0:
            return head

        for _ in range(k):
            current = head
            prev = None
            while current.next:
                prev = current
                current = current.next
            
            current.next = head
            head = current
            prev.next = None
        
        return head


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        """
        if not head:
            return head

        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        k %= length

        current.next = head

        current = head
        for _ in range(length - k - 1):
            current = current.next
        
        ans = current.next
        current.next = None

        return ans


def makeLinkedList(nums: List) -> ListNode:
    """
    utility function: make linked list from array
    """
    dummy_head = ListNode(-1)
    current = dummy_head
    for val in nums:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def printLinkedList(node: ListNode) -> None:
    """
    utility function: print all elements of linked list
    """
    print('---------------------------------')
    
    while node:
        print(f'[{node.val}]', end=' -> ')
        node = node.next
    
    print('', end='\n')


if __name__ =='__main__':
    solution = Solution()

    nums = [x for x in range(1, 6)]
    head = makeLinkedList(nums)
    k = 2
    printLinkedList(head)
    output_node = solution.rotateRight(head, k)
    printLinkedList(output_node)

    nums = [x for x in range(0, 3)]
    head = makeLinkedList(nums)
    k = 4
    printLinkedList(head)
    output_node = solution.rotateRight(head, k)
    printLinkedList(output_node)
