'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root

        return_node = None
        if root.left is not None:
            return_node = self.searchBST(root.left, val)
        if return_node is not None:
            return return_node

        if root.right is not None:
            return_node = self.searchBST(root.right, val)
        if return_node is not None:
            return return_node

        return return_node

    def print(self, root: TreeNode) -> None:
        if root is None:
            return
        print("val: ", root.val)
        if root.left is not None:
            self.print(root.left)
        if root.right is not None:
            self.print(root.right)


t4 = TreeNode(4)
t2 = TreeNode(2)
t7 = TreeNode(7)
t1 = TreeNode(1)
t3 = TreeNode(3)
t4.left = t2
t4.right = t7
t2.left = t1
t2.right = t3

solution = Solution()
node = solution.searchBST(t4, 2)
solution.print(node)
